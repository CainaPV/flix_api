from rest_framework.permissions import BasePermission

class PermissionsMovies(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('movies.view_movie')
        
        if request.method == 'POST':
            return request.user.has_perm('movies.add_movie')
        
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('movies.change_movie')
        return False