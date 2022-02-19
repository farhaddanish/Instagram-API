from django.contrib import admin
from .models import Posts



class AdminPost (admin.ModelAdmin):
    list_display = ("profile", "describtion", "date_of_post",)


admin.site.register(Posts, AdminPost)
