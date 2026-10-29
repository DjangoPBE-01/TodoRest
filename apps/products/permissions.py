from rest_framework.permissions import BasePermission, SAFE_METHODS  # Get, Option, head, GET 



class IsOwnerorReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user
    
    # def has_permission(self, request, view):
    #     if request.method in SAFE_METHODS:
    #         return True
    #     return request.user and request.user.is_authenticated
        
    # GET>>SAFE_METHODS