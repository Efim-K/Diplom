from rest_framework import permissions


class IsTeacher(permissions.BasePermission):
    """
    Класс для разрешения доступа только пользователей с группой "teacher"
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name="teacher").exists()


class IsOwner(permissions.BasePermission):
    """
    Класс для разрешения доступа только владельцам
    """

    def has_object_permission(self, request, view, object):
        if object.owner == request.user:
            return True
        return False
