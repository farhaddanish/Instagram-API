
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserFollowing_serializers, Followers_serializer, Following_serializer
from rest_framework import serializers
from profile_user.models import Profile_users
from .models import UserFollowing
from rest_framework.permissions import IsAuthenticated


class MakeFollowGV(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowing_serializers

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        user = self.request.user
        profile_follower = Profile_users.objects.get(pk=pk)
        profile_following = Profile_users.objects.get(user=user)

        if profile_following.user.username == profile_follower.user.username:
            raise serializers.ValidationError("same user is not allowed")

        userCheck = UserFollowing.objects.filter(
            followers=profile_follower, following=profile_following).exists()

        if userCheck:
            raise serializers.ValidationError("you allready follow that")

        profile_follower.followers_count += 1
        profile_follower.save()
        profile_following.following_count += 1
        profile_following.save()
        serializer.save(following=profile_following,
                        followers=profile_follower)
        return serializer


class UnFollowGV (generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowing_serializers

    def perform_create(self, serializer):

        pk = self.kwargs["pk"]
        user = self.request.user
        profile_follower = Profile_users.objects.get(pk=pk)
        profile_following = Profile_users.objects.get(user=user)

        if profile_following.user.username == profile_follower.user.username:
            raise serializers.ValidationError("same user is not allowed")

        userCheck = UserFollowing.objects.filter(
            followers=profile_follower, following=profile_following).exists()

        if not userCheck:
            raise serializers.ValidationError("you dont have follow this")

        profile_follower.followers_count -= 1
        profile_follower.save()
        profile_following.following_count -= 1
        profile_following.save()

        user = UserFollowing.objects.filter(
            followers=profile_follower, following=profile_following).delete()

        return Response(status=status.HTTP_200_OK)


class AllFollowers (generics.ListAPIView):

    queryset = UserFollowing.objects.all()
    serializer_class = Followers_serializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        profile = Profile_users.objects.get(pk=pk)
        followers = UserFollowing.objects.filter(followers=profile)
        return followers


class AllFollowing (generics.ListAPIView):

    queryset = UserFollowing.objects.all()
    serializer_class = Following_serializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        profile = Profile_users.objects.get(pk=pk)
        following = UserFollowing.objects.filter(following=profile)
        return following
