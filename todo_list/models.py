from django.db import models
from django.contrib.auth.models import User as DjangoUser

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item +' | '+ str(self.completed)


class User(models.Model):
    django_user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=False) #  timestamp: When the item is created
    updated = models.DateTimeField(blank=False) #  timestamp: When the item is last updated

    def __str__(self):
        return self.email


class Todo(models.Model):
    name = models.CharField(blank=False, max_length=200)
    description = models.CharField(blank=True, max_length=200)
    # user id: Id of the user who owns this todo item
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    StatusType = models.TextChoices('NotStarted', 'OnGoing', 'Completed')
    status = models.CharField(blank=False, choices=StatusType.choices, max_length=10) # An enum of either: NotStarted, OnGoing, Completed
    created = models.DateTimeField(blank=False) #  timestamp: When the item is created
    updated = models.DateTimeField(blank=False) #  timestamp: When the item is last updated

    def __str__(self):
        return self.name
