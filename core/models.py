
from django.db import models
from django.utils.text import slugify
from markdownx.models import MarkdownxField


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = MarkdownxField()
    summary = MarkdownxField()
    cover_image_url = models.URLField()
    slug = models.CharField(max_length=255, null=True, blank=True)

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
