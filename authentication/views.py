from django.core.mail import send_mail
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import User
from authentication.serializers import UserCreateSerializer


class Home(TemplateView):
    template_name = "Home.html"


class UserCreateAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        user = serializer.save()
        subject = 'Welcome to Storis Bro'
        message = 'Thank you for registering on our website.'
        from_email = 'storisbro@email.com'
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)