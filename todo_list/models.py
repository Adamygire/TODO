from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item +' | '+ str(self.completed)

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class StatusType(models.TextChoices):
    NOTSTARTED = 'NotStarted', _('NotStarted')
    ONGOING    = 'OnGoing', _('OnGoing')
    COMPLETED  = 'Completed', _('Completed')


class Todo(models.Model):
    name = models.CharField(blank=False, max_length=200)
    description = models.CharField(blank=True, max_length=200)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(blank=False, default=StatusType.NOTSTARTED, choices=StatusType.choices, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
