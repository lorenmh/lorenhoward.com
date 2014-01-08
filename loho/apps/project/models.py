#PROJECT MODELS

from django.db import models

#for images
from PIL import Image
import os

from apps.tag.models import Tag

from django.template.defaultfilters import slugify

from common.snippet import unique_slugify, urlify

def path_and_rename(path, type_name, name):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            project_name = name
            new_name = project_name + '-' + type_name + '-image'
            new_path = project_name + '/' + type_name + '/'
            filename = '{}.{}'.format(new_name, ext)
            return os.path.join(path + new_path, filename)
        return wrapper

class Project(models.Model):
    title = models.CharField(max_length = 256)
    url = models.SlugField(max_length=256)
    main_image = models.ImageField(blank = True, null = True, upload_to = 'project/main/')
    publish = models.BooleanField(default=False)
    weight = models.IntegerField()
    teaser = models.TextField()
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        unique_slugify(self, self.url)
        super(Project, self).save(*args, **kwargs)

class ShowcaseCode(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=256)
    publish = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    code = models.TextField()

    def __unicode__(self):
        return self.title

class ShowcaseImage(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=256)
    publish = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def change_name(instance,filename):
        fname, dot, extension = filename.rpartition('.')
        slug = urlify(instance.title)
        new_name = "%s.%s" % (slug,extension)
        return ('project/showcase/image/' + new_name)

    image = models.ImageField(upload_to=change_name)

    def __unicode__(self):
        return self.title

class ProjectLog(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=256)
    publish = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __unicode__(self):
        return self.title