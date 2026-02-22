from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=[('doctor','Doctor'), ('patient','Patient')])

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','phone_number','address','role']

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        phone = validated_data.pop('phone_number')
        address = validated_data.pop('address')
        role = validated_data.pop('role')

        user = User.objects.create_user(**validated_data, 
                                        first_name=first_name, 
                                        last_name=last_name)

        Profile.objects.create(user=user, phone_number=phone, address=address, role=role)

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            from django.contrib.auth import authenticate
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid username or password")
        else:
            raise serializers.ValidationError("Both username and password are required")

        data['user'] = user
        return data