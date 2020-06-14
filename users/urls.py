from users.views import ProjectUserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', ProjectUserViewSet, basename='user')
urlpatterns = router.urls
