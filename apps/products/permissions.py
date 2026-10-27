from rest_framework.permissions import BasePermission, SAFE_METHODS  # Get, Option, head, GET POST DELETE



class IsOwnerOrReadOnly(BasePermission):
     def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user
        
    # GET>>SAFE_METHODS