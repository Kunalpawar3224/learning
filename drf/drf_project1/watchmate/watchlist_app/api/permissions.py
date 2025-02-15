from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        '''
        Check if the user is an admin or the request method is GET.
        If the user is an admin provide crud permissions to admin
        '''
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or admin_permission
 