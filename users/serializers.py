from djoser.serializers import UserCreateSerializer
from . import models


# User Serializer 
class UserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'username', 'password', 'avatar')