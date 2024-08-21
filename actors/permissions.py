from rest_framework.permissions import BasePermission

class PermissionsActors(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('actors.view_actor')
        
        if request.method == 'POST':
            return request.user.has_perm('actors.add_actor')
        
        if request.method in ['PUT','PATCH']:
            return request.user.has_perm('actors.change_actor')
                
        return False