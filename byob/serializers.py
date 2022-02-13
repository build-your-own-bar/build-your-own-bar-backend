from rest_framework import serializers
from .models import Drink, Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    drink = serializers.HyperlinkedRelatedField(
        view_name='drink_detail', read_only=True)
    drink_id = serializers.PrimaryKeyRelatedField(
        queryset=Drink.objects.all(),
        source='drink'
    )

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'title', 'drink',
                  'body', 'owner', 'drink_id')


class DrinkSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    drink_url = serializers.ModelSerializer.serializer_url_field(
        view_name='drink_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Drink
        fields = ('id', 'name', 'ice', 'spirit', 'liqueur', 'juice', 'garnish',
                  'citrus', 'soda', 'special_request', 'photo', 'owner', 'comments', 'drink_url')
