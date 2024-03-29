"""
URL configuration for storis_bro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from ref.views import referral_view, register_referral

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('authentication.urls', 'authentication'), namespace='authentication')),
    path('notification/', include(('notification.urls', 'notification'), namespace='notification')),
    path('profiles/update/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('referral/<int:referral_number>/', referral_view, name='referral_view'),
    path('register_referral/', register_referral, name='register_referral'),
]