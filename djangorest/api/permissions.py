from rest_framework.permissions import BasePermission
from tasklist.models import Tasklist


class IsOwner(BasePermission):
    """Custom permission class to allow only tasklist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the tasklist owner."""
        if isinstance(obj, Tasklist):
            return obj.owner == request.user
        return obj.owner == request.user