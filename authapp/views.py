from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializers
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
