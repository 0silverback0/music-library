from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Beat, CustomUser
from .serializers import BeatSerializer, CustomUserSerializer
import logging

# Set up logging
logger = logging.getLogger(__name__)

class UserBeatCreateView(generics.CreateAPIView):
    """
    Create a new beat. Accessible to authenticated users.
    """
    serializer_class = BeatSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(producer=self.request.user)
            logger.info(f"Beat created by user {self.request.user.username}")
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            raise ValidationError(e)

class UserApprovedBeatListView(generics.ListAPIView):
    """
    View all approved beats. Accessible to authenticated users.
    """
    serializer_class = BeatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Beat.objects.filter(status='approved')

class UserOwnBeatListView(generics.ListAPIView):
    """
    View all beats created by the authenticated user. Accessible to authenticated users.
    """
    serializer_class = BeatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Beat.objects.filter(producer=self.request.user)

class UserPendingBeatUpdateView(generics.UpdateAPIView):
    """
    Update a pending beat created by the authenticated user. Accessible to authenticated users.
    """
    serializer_class = BeatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Beat.objects.filter(producer=self.request.user, status='pending')

    def perform_update(self, serializer):
        try:
            serializer.save()
            logger.info(f"Beat updated by user {self.request.user.username}")
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            raise ValidationError(e)

class UserPendingBeatDeleteView(generics.DestroyAPIView):
    """
    Delete a pending beat created by the authenticated user. Accessible to authenticated users.
    """
    serializer_class = BeatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Beat.objects.filter(producer=self.request.user, status='pending')

    def perform_destroy(self, instance):
        try:
            instance.delete()
            logger.info(f"Beat deleted by user {self.request.user.username}")
        except Exception as e:
            logger.error(f"Error deleting beat: {e}")
            raise ValidationError(e)

class UserRegistrationView(generics.CreateAPIView):
    """
    Register a new user. Accessible to anyone.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        try:
            serializer.save()
            logger.info(f"New user registered: {serializer.instance.username}")
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            raise ValidationError(e)
