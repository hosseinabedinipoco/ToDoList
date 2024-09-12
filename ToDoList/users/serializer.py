from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password':"passwords must be same"})
        return data

    def create(self, data):
        user = User.objects.create(
            email = data['email'],
            username = data['username'],
            password = make_password(data['password'])
        )
        return user