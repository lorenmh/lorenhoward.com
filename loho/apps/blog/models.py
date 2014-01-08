from django.db import models

from apps.tag.models import Tag
from apps.comment.models import Comment

from common.snippet import unique_slugify, urlify

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=256)
    url = models.SlugField()
    publish = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    teaser = models.TextField(blank=True, null=True)
    text = models.TextField()

    generic.GenericRelation(Comment)

    def __unicode__(self):
        return (self.title)

    def save(self, *args, **kwargs):
        unique_slugify(self, self.url)
        super(Blog, self).save(*args, **kwargs)

class BlogImage(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)

    def change_name(instance, filename):
        fname, dot, extension = filename.rpartition('.')
        slug = urlify(instance.title)
        new_name = "%s.%s" % (slug,extension)
        return ('blog/image/' + new_name)

    image = models.ImageField(upload_to=change_name)

    def __unicode__(self):
        return self.title