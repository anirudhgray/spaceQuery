from rest_framework import permissions


class IsSaveAccess(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "PUT" or request.method == "PATCH":
            return False
        return obj.user == request.user or request.user.is_admin
