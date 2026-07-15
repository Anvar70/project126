from django.shortcuts import render
from .serializers import ProductsSerializer
from rest_framework.generics import  ListAPIView,CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer

class UserViews(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDelete(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer