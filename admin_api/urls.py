from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    AdminUserListView,
    AdminUserDetailView,
    AdminUserCreateView,
    AdminUserUpdateView,
    AdminUserDeleteView,
    AdminBeatListView,
    AdminBeatDetailView,
    AdminBeatCreateView,
    AdminBeatUpdateView,
    AdminBeatDeleteView
)

urlpatterns = [
    path('users/', AdminUserListView.as_view(), name='admin-user-list'),
    path('users/<int:pk>/', AdminUserDetailView.as_view(), name='admin-user-detail'),
    path('users/create/', AdminUserCreateView.as_view(), name='admin-user-create'),
    path('users/<int:pk>/update/', AdminUserUpdateView.as_view(), name='admin-user-update'),
    path('users/<int:pk>/delete/', AdminUserDeleteView.as_view(), name='admin-user-delete'),
    
    path('beats/', AdminBeatListView.as_view(), name='admin-beat-list'),
    path('beats/<int:pk>/', AdminBeatDetailView.as_view(), name='admin-beat-detail'),
    path('beats/create/', AdminBeatCreateView.as_view(), name='admin-beat-create'),
    path('beats/<int:pk>/update/', AdminBeatUpdateView.as_view(), name='admin-beat-update'),
    path('beats/<int:pk>/delete/', AdminBeatDeleteView.as_view(), name='admin-beat-delete'),

    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

