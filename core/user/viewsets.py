
# Create your views here.
from rest_framework import permissions

from core.user.models import User
from core.user.serializers import UserSerializer
from core.abstract.viewsets import AbstractViewSet


class UserViewSet(AbstractViewSet):
    http_method_names = ("patch", "get")
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()

        return User.objects.exclude(is_superuser=True)

    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
