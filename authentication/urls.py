from django.urls import path, include
from django.contrib.auth import views as auth_views
from authentication.views import Home, UserCreateAPIView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('home/', Home.as_view(), name='home')
]
