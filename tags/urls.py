from tags.views import TagsViewSet
from rest_framework.routers import DefaultRouter

app_name = 'tags'

router = DefaultRouter()
router.register(r'tags', TagsViewSet, basename='tags')
urlpatterns = router.urls
