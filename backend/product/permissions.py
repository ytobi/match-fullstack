from rest_framework.permissions import BasePermission
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS or
            (request.user and request.user.is_authenticated and obj.sellerId.id == request.user.id))
