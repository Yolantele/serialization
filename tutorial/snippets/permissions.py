from rest_framework import permissions 

class IsOwnerOrReadOnly(permissions.BasePermission):
    #custom permission to allow owners of object to edit it

    def has_object_permission(self, request, view, object):
        #read permissions are allowed to any request, so we will allow GET, HEAD or OPTIONS requests:
        if request.method in permissions.SAFE_METHODS:
            return True
        #write permissions are only allowed to the owner of snippet. 
        return obj.owner == request.user
        