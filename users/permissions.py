from rest_framework import permissions


class SuperUserOrReadOnly(permissions.BasePermission):
    """
    Allows only superuser to perform requests that change DB state

    If user is superuser it can do anything.
    If user is not superuser it can perform GET and POST requests, but can not edit other user objects.
    """

    def has_permission(self, request, view):
        return request.method not in ['GET', 'POST'] and (request.user and not request.user.is_superuser)
