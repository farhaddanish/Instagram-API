from django.db import models
from profile_user.models import Profile_users
# Create your models here.


class UserFollowing (models.Model):
    # the person that we want to follow
    following = models.ForeignKey(
        Profile_users, on_delete=models.CASCADE, related_name="following_user")
    # iam that i want to follow
    followers = models.ForeignKey(
        Profile_users, on_delete=models.CASCADE, related_name="followers_user")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.following.user.username + " is follow " + self.followers.user.username
