from apps.tag.models import Tag

from django import forms
from django.contrib import admin

class TagAdmin(admin.ModelAdmin):
    exclude = ['url']

admin.site.register(Tag, TagAdmin)
