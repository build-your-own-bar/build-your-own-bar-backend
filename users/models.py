from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=250, unique=True)
    avatar = models.CharField(max_length=500)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    birthday = models.CharField(max_length=100)
    my_drinks = ArrayField(models.CharField(
        max_length=100, blank=True), default=list)

    def get_username(self):
        return self.email
