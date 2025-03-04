from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'producer_name', 'pro', 'pro_number', 'is_superuser']
        read_only_fields = ['id']

from rest_framework import serializers
from .models import Beat
from users.serializers import CustomUserSerializer  # If you want to include user details in the Beat serializer

class BeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beat
        fields = ['id', 'producer', 'title', 'genre', 'bpm', 'status', 'price', 'file_url', 'created_at']