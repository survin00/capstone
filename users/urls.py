from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import (
	UserRegistrationAPIView,
	UserLoginAPIView,
	UserViewAPI,
	UserLogoutViewAPI,
)


urlpatterns = [
	path('register/', UserRegistrationAPIView.as_view()),
	path('login/', UserLoginAPIView.as_view()),
	path('view/', UserViewAPI.as_view()),
	path('logout/', UserLogoutViewAPI.as_view()),
]