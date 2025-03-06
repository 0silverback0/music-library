from rest_framework import serializers
from .models import CustomUser, Beat

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model. Handles password hashing.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'producer_name', 'first_name', 'last_name', 'pro', 'pro_number']
        read_only_fields = ['id']

    def create(self, validated_data):
        """
        Create a new user with hashed password.
        """
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            producer_name=validated_data['producer_name'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            pro=validated_data.get('pro', ''),
            pro_number=validated_data.get('pro_number', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class BeatSerializer(serializers.ModelSerializer):
    """
    Serializer for Beat model.
    """
    class Meta:
        model = Beat
        fields = ['id', 'producer', 'title', 'genre', 'bpm', 'status', 'price', 'file_url', 'created_at']
        read_only_fields = ['id', 'producer', 'created_at']