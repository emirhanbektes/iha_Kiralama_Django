from rest_framework import serializers
from product.models import Product



class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'imageUrl', 'date', 'weight', 'category']

    def update(self,instance,validated_data):
        instance.title = validated_data.get("title",instance.title)
        instance.description = validated_data.get("description",instance.description)
        instance.weight = validated_data.get("weight",instance.weight)
        instance.date = validated_data.get("date",instance.date)
        instance.save()
        return instance