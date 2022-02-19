
from rest_framework import serializers
from .serilaizers import Profile_serializers, User_serializers
from rest_framework import generics
from rest_framework.response import Response
from .models import Profile_users
from django.contrib.auth.models import User
from . import signals
from rest_framework.views import APIView
from . import permission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import filters
# Create your views here.


class UserCreationGV (generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_serializers

    def perform_create(self, serializer):
        data = {}
        account = serializer.save()
        token = Token.objects.get(user=account).key
        data["token"] = token
        data["user"] = account.username
        return data


class AllProfileGV (generics.ListAPIView):
    
    queryset = Profile_users.objects.all()
    serializer_class = Profile_serializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'bio']


class ProfileDetailGV (generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    permission_classes = [permission.IsSingleUpdate]

    queryset = Profile_users.objects.all()
    serializer_class = Profile_serializers


class SingleProfileGV(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    permission_classes = [permission.IsSingleUpdate]

    queryset = Profile_users.objects.all()
    serializer_class = Profile_serializers
