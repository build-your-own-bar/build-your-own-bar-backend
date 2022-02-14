from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from . import models


# User Serializer
class UserCreateSerializer(UserCreateSerializer):
    # users = serializers.HyperlinkedModelSerializer(
    #     view_name='user_detail', read_only=True)

    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'username', 'password',
                  'avatar', 'birthday', 'my_drinks')
