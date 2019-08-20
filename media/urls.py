from media.views import MediaViewSet
from rest_framework.routers import DefaultRouter

app_name = 'media'

router = DefaultRouter()
router.register(r'media', MediaViewSet, basename='media')
urlpatterns = router.urls
