from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from users.models import Beat, CustomUser
from users.serializers import BeatSerializer, CustomUserSerializer

# Admin User CRUD Views
class AdminUserListView(generics.ListAPIView):
    """
    View all users. Accessible only to admin users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this view

class AdminUserDetailView(generics.RetrieveAPIView):
    """
    View details of a single user. Accessible only to admin users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this view

class AdminUserCreateView(generics.CreateAPIView):
    """
    Create a new user. Accessible only to admin users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this view

class AdminUserUpdateView(generics.UpdateAPIView):
    """
    Update an existing user. Accessible only to admin users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this view

class AdminUserDeleteView(generics.DestroyAPIView):
    """
    Delete a user. Accessible only to admin users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this view


# Admin Beat CRUD Views
class AdminBeatListView(generics.ListAPIView):
    """
    View all beats. Accessible only to admin users.
    """
    queryset = Beat.objects.all()
    serializer_class = BeatSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this view

class AdminBeatDetailView(generics.RetrieveAPIView):
    """
    Retrieve beat details by ID. Accessible only to admin users.
    """
    queryset = Beat.objects.all()
    serializer_class = BeatSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this view

class AdminBeatCreateView(generics.CreateAPIView):
    """
    Create new beats. Accessible only to admin users.
    """
    queryset = Beat.objects.all()
    serializer_class = BeatSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this view

class AdminBeatUpdateView(generics.UpdateAPIView):
    """
    Update beat details. Accessible only to admin users.
    """
    queryset = Beat.objects.all()
    serializer_class = BeatSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this view

class AdminBeatDeleteView(generics.DestroyAPIView):
    """
    Delete a beat. Accessible only to admin users.
    """
    queryset = Beat.objects.all()
    serializer_class = BeatSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this view
