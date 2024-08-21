from rest_framework.permissions import BasePermission


class PermissionsGenres(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['GET', 'HEAD', 'OPTIONS' ]:
            return request.user.has_perm('genres.view_genre')
        
        return False
        