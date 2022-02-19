from django.contrib import admin
from .models import UserFollowing




class AdminFollow (admin.ModelAdmin):
    list_display = ("following","followers","created",)

admin.site.register(UserFollowing,AdminFollow)
