from django.contrib import auth
from django.db import models

class ContentFormat(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Note(models.Model):
    user = models.ForeignKey(
        auth.get_user_model(),
        on_delete=models.CASCADE,
        related_name='notes'
    )

    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    content_format = models.ForeignKey(ContentFormat, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
