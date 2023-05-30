from rest_framework_nested import routers

from Core.user.viewsets import UserViewSet
from Core.auth.viewsets.login import LoginViewSet
from Core.auth.viewsets.register import RegisterViewSet
from Core.auth.viewsets.refresh import RefreshViewSet

router = routers.SimpleRouter()

router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    *router.urls,
]