from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        '''
        Check if the user is an admin or the request method is GET.
        If the user is an admin provide crud permissions to admin
        '''
        # admin_permission = bool(request.user and request.user.is_staff)
        # return request.method == "GET" or admin_permission

        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            # Check permissions for write request
            return bool(request.user and request.user.is_staff)
 

class IsReviewUserorReadOnly(permissions.BasePermission):
    ''''
    If the user is a review owner then only he has all he permissions otherwise
    other user can have only get permissions
    '''

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            # Check permissions for write request
            return obj.review_user == request.user