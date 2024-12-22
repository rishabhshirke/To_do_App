from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # Date = models.DateField(blank=False)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
