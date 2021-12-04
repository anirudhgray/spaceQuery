from rest_framework import permissions


class CanPost(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return False


class IsUserAccess(permissions.BasePermission):
    message = "You are not authorized to access other users."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "DELETE":
            return request.user.is_admin
        return obj == request.user or request.user.is_admin


class IsProfileAccess(permissions.BasePermission):
    message = "You are not authorized to access other users."

    def has_permission(self, request, view):
        if request.method != "POST":
            return True
        if not request.user.is_authenticated:
            return True
        return request.user.is_admin

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "DELETE":
            return False
        return obj.user == request.user or request.user.is_admin
