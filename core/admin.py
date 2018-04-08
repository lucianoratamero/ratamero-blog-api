from django.contrib import admin

from core import models
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(models.BlogPost, MarkdownxModelAdmin)
