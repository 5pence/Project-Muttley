from comments.views import CommentViewSet
from rest_framework.routers import DefaultRouter

app_name = 'comments'

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comments')
urlpatterns = router.urls
