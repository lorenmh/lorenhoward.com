from apps.project.models import Project, ShowcaseCode, ShowcaseImage, ProjectLog

from django.contrib import admin
from django import forms

class ShowcaseCodeInline(admin.StackedInline):
    extra = 1
    model = ShowcaseCode

class ShowcaseImageInline(admin.StackedInline):
    extra = 3
    model = ShowcaseImage

class ProjectLogInline(admin.StackedInline):
    extra = 1
    model = ProjectLog

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectLogInline, ShowcaseCodeInline, ShowcaseImageInline,]
    filter_horizontal = ['tags',]
    prepopulated_fields = {"url": ("title",)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectLog)
admin.site.register(ShowcaseImage)
admin.site.register(ShowcaseCode)