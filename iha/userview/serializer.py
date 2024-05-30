from rest_framework import serializers
from userview.models import UserProfile
from django.contrib.auth.models import User
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'imageUrl', 'date', 'weight', 'category']



class userSerializer(serializers.ModelSerializer):
    product_details = serializers.SerializerMethodField()
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id','user', 'startdate', 'stopdate', 'product', 'product_details', 'user_details']

    def get_product_details(self, obj):
        try:
            product = Product.objects.get(id=obj.product)
            return ProductSerializer(product).data
        except Product.DoesNotExist:
            return None

    def get_user_details(self, obj):
        try:
            user = User.objects.get(id=obj.user)
            return {'id': user.id, 'username': user.username}
        except User.DoesNotExist:
            return None

    def update(self, instance, validated_data):        
        instance.startdate = validated_data.get("startdate", instance.startdate)
        instance.stopdate = validated_data.get("stopdate", instance.stopdate)        
        instance.save()
        return instance
    
    def get_user_profile(self, user_id):
        try:
            user_profile = UserProfile.objects.get(user=user_id)
            # Include the user profile ID in the serialized data
            serialized_data = self.to_representation(user_profile)
            serialized_data['id'] = user_profile.id  # Add the ID to the dictionary
            return serialized_data
        except UserProfile.DoesNotExist:
            return None