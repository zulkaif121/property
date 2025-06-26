# users/serializers.py
from rest_framework import serializers
from accounts.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone_number', 'address', 'full_name']
        
    def create(self, validated_data):
        """
        Create a new user with hashed password.
        """
        password = validated_data.pop('password')  
        user = super().create(validated_data)  
        user.set_password(password)  
        user.save() 
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'address', 'full_name']
        
