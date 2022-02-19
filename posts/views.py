
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Posts
from .serializers import Post_serializers
from profile_user.models import Profile_users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .permission import PostUpdatePermission
from rest_framework import filters
# Create your views here.


class AllPostGV (generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = Post_serializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['describtion',]

    def get_queryset(self):
        pk = self.kwargs["pk"]
        try:
            profile = Profile_users.objects.get(pk=pk)
        except:
            raise serializers.ValidationError("muching query does not exist")
        post = Posts.objects.filter(profile=profile)

        return post


class CreatePostGV (generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Posts.objects.all()
    serializer_class = Post_serializers

    def perform_create(self, serializer):
        user = self.request.user
        profile = Profile_users.objects.get(user=user)
        profile.posts_count += 1
        profile.save()
        serializer.save(profile=profile)
        return serializer


class SinglePostGV (APIView):
    permission_classes = [PostUpdatePermission, IsAuthenticated]

    def get(self, request, pk, pk2):
        post = Posts.objects.get(pk=pk2)
        serializer = Post_serializers(post)
        return Response(serializer.data)

    def put(self, request, pk, pk2):
        post = Posts.objects.get(pk=pk2)
        self.check_object_permissions(request, post)
        serializer = Post_serializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    def delete(self, request, pk, pk2):
        post = Posts.objects.get(pk=pk2)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_200_OK)
