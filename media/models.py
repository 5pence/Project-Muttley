import uuid
from django.db import models

from tags.models import Tag
from user.models import User


class Media(models.Model):
    MEDIA_CHOICES = [
        ['image', 'Image'],
        ['video', 'Video']
    ]

    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    file = models.FileField()
    type = models.CharField(choices=MEDIA_CHOICES, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
