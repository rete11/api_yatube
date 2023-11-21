from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    """Класс AuthorPermission наследует от базового класса BasePermission.
    Данный класс определяет, имеет ли пользователь право
    операции (чтения, обновления, удаления) над определенным объектом"""
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
