from django.db import models
from apps.tag.models import Tag

class Service(models.Model):
    title = models.CharField(max_length=128)
    caption = models.CharField(max_length=128)
    brief_descripton = models.TextField()
    description = models.TextField()
    weight = models.PositiveIntegerField()
    color = models.CharField(max_length=64)

#MAKE SURE TO ADD PROMOTIONAL IMAGES SECTION / EXAMPLE OF WORK

    def __unicode__(self):
        return (self.title)

    def save(self, *args, **kwargs):
        self.url_name = str.join('-', [string for string in self.title.split(' ') if string])
        super(Article, self).save(*args, **kwargs)
