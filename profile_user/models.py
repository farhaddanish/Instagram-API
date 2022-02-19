

from django.db import models
from django.contrib.auth.models import User


class Profile_users (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_models")
    bio = models.CharField(max_length=100)
    number = models.IntegerField(null=True)
    posts_count = models.IntegerField(default=0)

    following_count = models.IntegerField(default=0)
    followers_count = models.IntegerField(default=0)
    

    def __str__(self):
        return self.user.username
