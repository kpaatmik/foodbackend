from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, min_length=3, required=True)
    password = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100, required=True)
    phone_number = serializers.CharField(max_length = 15,required=False)
    address = serializers.CharField(max_length=250,required=False)
    
    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username already exists")
        return username

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        #phone_number = validated_data['phone_number']
        #address = validated_data['address']
        user = User.objects.create(
            username=username,password=password,first_name=first_name,last_name=last_name,email=email
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, min_length=3, required=True)
    password = serializers.CharField(max_length=200)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodListing
        #fields = '__all__'
        exclude = ['created_at','visibilty']
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'