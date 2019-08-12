import uuid

from django.db import models


class Tag(models.Model):
    """
    Holds the tags.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(default=None, blank=False, null=False, max_length=60)
