"""Models settings."""
from django.db import models


class Todo(models.Model):
    """Model todo."""

    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        """Str return title."""
        return self.title
