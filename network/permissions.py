from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """Класс для роли активного сотрудника"""
    def has_permission(self, request, view):
        """Метод для определения принадлежности пользователя к активным сотрудникам"""
        return request.user.is_active
