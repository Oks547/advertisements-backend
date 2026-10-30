from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешаем всем читать (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
           
        # Разрешаем изменять/удалять только создателю объявления
        return obj.creator == request.user