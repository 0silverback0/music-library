from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users.views import (
    UserBeatCreateView,
    UserApprovedBeatListView,
    UserOwnBeatListView,
    UserPendingBeatUpdateView,
    UserPendingBeatDeleteView,
    UserRegistrationView  # Import the new view
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete()
        return Response(status=204)

urlpatterns = [
    # User Beat Views
    path('user/beats/create/', UserBeatCreateView.as_view(), name='user-beat-create'),
    path('user/beats/approved/', UserApprovedBeatListView.as_view(), name='user-approved-beat-list'),
    path('user/beats/', UserOwnBeatListView.as_view(), name='user-own-beat-list'),
    path('user/beats/<int:pk>/update/', UserPendingBeatUpdateView.as_view(), name='user-pending-beat-update'),
    path('user/beats/<int:pk>/delete/', UserPendingBeatDeleteView.as_view(), name='user-pending-beat-delete'),

    # User Registration View
    path('user/register/', UserRegistrationView.as_view(), name='user-register'),

    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # User Login and Logout Views
    path('user/login/', ObtainAuthToken.as_view(), name='user-login'),
    path('user/logout/', LogoutView.as_view(), name='user-logout'),
]