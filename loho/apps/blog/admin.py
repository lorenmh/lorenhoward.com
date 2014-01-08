from apps.blog.models import Blog, BlogImage

from apps.comment.models import Comment

from django.contrib.contenttypes import generic

from django import forms
from django.contrib import admin

class CommentInline(generic.GenericStackedInline):
    model = Comment
    extra = 0
    readonly_fields = ('name','email','subject','text',)

class BlogImageInline(admin.StackedInline):
    extra = 3
    model = BlogImage

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline, BlogImageInline];
    filter_horizontal = ['tags',]
    prepopulated_fields = {"url": ("title",)}

admin.site.register(Blog, BlogAdmin)
