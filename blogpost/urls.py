from blogpost.views import BlogPostViewSet
from rest_framework.routers import DefaultRouter

app_name = 'blogpost'

router = DefaultRouter()
router.register(r'blogposts', BlogPostViewSet, basename='blog_posts')
urlpatterns = router.urls
