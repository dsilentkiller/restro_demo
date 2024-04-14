from rest_framework import serializers
from app.models import Menu


class MenuSerializers(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=True,max_length=100)
    # price = serializers.FloatField(required=True)
    class Meta:
        model = Menu
        fields = ['name', 'price']

    def create(self, validated_data):
        '''create and return menu instance given validated data'''
        return Menu.objects.create(**validated_data)

    def update(self, instance, validated_data):
        '''update and return an existing  data ,given validated data'''
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
