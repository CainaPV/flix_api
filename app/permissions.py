from rest_framework.permissions import BasePermission

class GlobalPermissions(BasePermission):
    
    def has_permission(self, request, view):
        model_permissions = self._get_model_permission(method = request.method, view=view,)

        if not model_permissions:
            return False
        
        return request.user.has_perm(model_permissions)
    
    
    def _get_model_permission(self, method, view):
        try:
            app_label = view.queryset.model._meta.app_label
            method_actions = self.get_method_actions(method)
            model_name = view.queryset.model._meta.model_name
            return f'{app_label}.{method_actions}_{model_name}'
        except AttributeError:
            return None    

    def get_method_actions(self, method):
        actions = {'GET': 'view', 'OPTIONS':'view', 'HEAD': 'view', 'POST': 'add', 'PUT': 'change', 'PATCH': 'change', 'DELETE': 'delete'}
        return actions.get(method or '')
          
    