import uuid

from django.db import models


class Category(models.Model):
    """
    Holds the category.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(default=None, blank=False, null=False, max_length=100)
    description = models.CharField(default=None, blank=True, null=True, max_length=200)
