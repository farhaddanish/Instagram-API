
from rest_framework import serializers
from .models import Posts


class Post_serializers (serializers.ModelSerializer):
    profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Posts
        # exclude = ["profile"]
        fields = "__all__"
