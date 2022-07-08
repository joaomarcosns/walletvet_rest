#App
from .views import UserViewSet

# Framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet), 
urlpatterns = router.urls