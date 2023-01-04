from django.http import Http404
from rest_framework import generics, viewsets, status, views
from todo_list.models import Todo, User
from .serializers import TodoSerializer, UserSerializer
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.utils import timezone
from django.contrib.auth import authenticate, login


class TodoListView(views.APIView):
    @action(detail=False,
            methods=['get'])
    def get(self, request, *args, **kwargs):
        status = request.query_params.get('status', 'all')
        print(status)
        if status == 'all':
            queryset = Todo.objects.all()
        else:
            queryset = Todo.objects.filter(status=status)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False,
            methods=['post'])
    def post(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    @action(detail=False,
            methods=['get'])
    def get(self, request, pk, *args, **kwargs):
        serializer = TodoSerializer(self.get_object(pk))
        return Response(serializer.data)

    @action(detail=False,
            methods=['put'])
    def put(self, request, pk, *args, **kwargs):
        data = request.data
        data['updated'] = timezone.now()
        serializer = TodoSerializer(self.get_object(pk), data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False,
            methods=['delete'])
    def delete(self, request, pk, *args, **kwargs):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get_users(request):
    snippets = User.objects.all()
    serializer = UserSerializer(snippets, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        User.objects.create_user(request.data['email'], request.data['password'])
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signin(request):
    print('signin: ', request.data)
    email, password= request.data['email'], request.data['password']
    user = authenticate(request, email=email, password=password)
    if user != None:
        login(request, user)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def changePassword(request, pk):
    user = User.objects.get(pk)
    print(request.data)
    if request.data.get('password', False):
        user.set_password(request.data['password'])
        return Response(status=status.HTTP_200_OK)
    return Response('Missing password!', status=status.HTTP_400_BAD_REQUEST)


class UserListView(views.APIView):
    @action(detail=False,
            methods=['get'])
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False,
            methods=['post'])
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(views.APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

