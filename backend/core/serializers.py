from rest_framework import serializers
from .models import List,Item
from .models import User
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Item
        fields = ['id','name','list','done','url']

class ListSerializer(serializers.HyperlinkedModelSerializer):
    item_set = ItemSerializer(many=True)
    class Meta:
        model= List
        fields = ['id','name','owner','url','item_set']

    def create(self, validated_data):
        items_data = validated_data.pop('item')
        list = List.objects.create(**validated_data)
        for items_data in items_data:
            Item.create(list=list, **items_data)

        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    username = serializers.CharField(required=True)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance