
from django.db import models
from markdownx.models import MarkdownxField


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = MarkdownxField()
    summary = MarkdownxField()
    cover_image_url = models.URLField()
