
from rest_framework import serializers
from .models import Profile_users
from django.contrib.auth.models import User
from followApp.serializers import Following_serializer, Followers_serializer


class User_serializers (serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "password2"]

    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError("password must be the same")

        user = User.objects.create(
            username=self.validated_data["username"], email=self.validated_data["email"])

        user.set_password(password)
        user.save()
        return user


class Profile_serializers (serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    posts_count = serializers.StringRelatedField(read_only=True)
    following_count = serializers.StringRelatedField(read_only=True)
    followers_count = serializers.StringRelatedField(read_only=True)

    following_user = serializers.SerializerMethodField()
    followers_user = serializers.SerializerMethodField()

    class Meta:
        model = Profile_users
        fields = "__all__"

    def get_following_user(self, obj):
        return Following_serializer(obj.following_user.all(), many=True).data

    def get_followers_user(self, obj):
        return Followers_serializer(obj.followers_user.all(), many=True).data
