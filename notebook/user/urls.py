from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.UserProfileListView.as_view(), name='all_users'),
    path('user/<int:pk>/', views.UserProfileDetailView.as_view(), name='user'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
]
