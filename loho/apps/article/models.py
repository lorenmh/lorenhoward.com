from django.db import models
from apps.tag.models import Tag

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128)
    url_name = models.CharField(max_length=128, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    text = models.TextField()

    def __unicode__(self):
        return (self.title)

    def save(self, *args, **kwargs):
        self.url_name = str.join('-', [x.lower() for x in self.title.split(' ') if x])
        supoer(Article, self).save(*args, **kwargs)
