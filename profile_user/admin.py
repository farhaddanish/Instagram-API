from django.contrib import admin
from .models import Profile_users


class AdminProfile (admin.ModelAdmin):
    list_display = ("user","number","posts_count",)


admin.site.register(Profile_users,AdminProfile)

