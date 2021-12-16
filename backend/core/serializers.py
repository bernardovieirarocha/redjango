from rest_framework import serializers
from .models import List,Item



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