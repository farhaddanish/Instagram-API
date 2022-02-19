from importlib import import_module
from rest_framework import serializers
from profile_user.models import Profile_users
from .models import UserFollowing


class UserFollowing_serializers (serializers.ModelSerializer):

    following = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='singlePrfoile'
    )
    followers = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='singlePrfoile'
    )

    class Meta:
        model = UserFollowing
        fields = "__all__"


class Following_serializer (serializers.ModelSerializer):
    following = serializers.StringRelatedField(read_only=True)
    followers = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserFollowing
        fields = "__all__"


class Followers_serializer (serializers.ModelSerializer):
    followers = serializers.StringRelatedField(read_only=True)
    following = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserFollowing
        fields = "__all__"
