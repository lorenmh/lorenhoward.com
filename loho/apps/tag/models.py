from django.db import models
from common.snippet import unique_slugify, urlify

class Tag(models.Model):
    name = models.CharField(max_length=128)
    url = models.SlugField()

    def __unicode__(self):
        return (self.name)

    def save(self, *args, **kwargs):
        unique_slugify(self, urlify(self.name))
        super(Tag, self).save(*args, **kwargs)