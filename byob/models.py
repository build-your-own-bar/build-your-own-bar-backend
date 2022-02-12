from django.db import models
from django import forms

# Create your models here.


class Drink(models.Model):
    name = models.CharField(max_length=100, default='no name')
    ice = models.CharField(max_length=100, default='no ice')
    spirit = models.CharField(max_length=100, default='no spirit')
    liqueur = models.CharField(max_length=100, default='no liqueur')
    juice = models.CharField(max_length=100, default='no juice')
    garnish = models.CharField(max_length=100, default='no garnish')
    citrus = models.CharField(max_length=100, default='no citrus')
    soda = models.CharField(max_length=100, default='no soda')
    special_request = models.TextField(null=True, blank=True)
    photo = models.ImageField(
        upload_to='images/', default='images/drank.jpg')
    owner = models.ForeignKey(
        'users.User', related_name='drinks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=100)
    drink = models.ForeignKey(
        Drink, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    owner = models.ForeignKey(
        'users.User', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
