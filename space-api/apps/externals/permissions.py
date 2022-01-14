from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """Allow non-safe methods to Admin Users only."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_admin
