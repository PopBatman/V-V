from rest_framework.permissions import IsAuthenticated

from Core.abstract.viewsets import AbstractViewSet
from Core.user.serializers import UserSerializer
from Core.user.models import User
from Core.auth.permissions import UserPermission

# Create your views here.

class UserViewSet(AbstractViewSet):
    http_method_names = ('patch', 'get')
    permissions_classes = (IsAuthenticated, UserPermission, )
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])

        self.check_object_permissions(self.request, obj)

        return obj