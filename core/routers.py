from rest_framework import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet

router = routers.SimpleRouter()

# auth
router.register(r'auth/register',RegisterViewSet, basename='auth-register')

# USER
router.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    *router.urls,
]