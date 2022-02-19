from rest_framework import permissions


class PostUpdatePermission (permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        else:
            return obj.profile.user == request.user
