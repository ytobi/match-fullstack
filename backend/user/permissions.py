from rest_framework.permissions import BasePermission
from .models import UserRole

class IsABuyer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == UserRole.BUYER