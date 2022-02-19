from django.db import models
from profile_user.models import Profile_users
# Create your models here.


class Posts (models.Model):
    profile = models.ForeignKey(
        Profile_users, on_delete=models.CASCADE, related_name="profile")
    describtion = models.TextField()
    date_of_post = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile.user.username
