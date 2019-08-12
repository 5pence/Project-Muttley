import uuid

from django.db import models
from django.utils.text import slugify

from media.models import Media
from user.models import User
from category.models import Category
from tags.models import Tag


class BlogPost(models.Model):
    """
    Holds the blog posts.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='user_id', on_delete=models.SET_NULL, null=True)
    title = models.CharField(default=None, blank=False, null=False, max_length=200)
    slug = models.SlugField(max_length=200, null=False, allow_unicode=True)
    body_text = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    media = models.ManyToManyField(Media, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(BlogPost, self).save(*args, **kwargs)
