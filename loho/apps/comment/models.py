from django.db import models
from django.forms import ModelForm

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

# Create your models here.
class Comment(models.Model):
    #for generic types, limits the models to blog and project
    limit = models.Q(app_label = 'blog', model = 'blog') | models.Q(app_label = 'project', model = 'project')
    content_type = models.ForeignKey(ContentType, limit_choices_to = limit)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    timestamp = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    text = models.TextField()

    def __unicode__(self):
        return self.text[:40]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'text']

    def __init__(self, *args, **kwargs):
        ct = None
        oid = None

        if 'content_type' in kwargs:
            ct = kwargs.pop('content_type')

        if 'object_id' in kwargs:
            oid = kwargs.pop('object_id')

        super(CommentForm, self).__init__(*args, **kwargs)

        if (ct):
            self.instance.content_type = ct

        if (oid):
            self.instance.object_id = oid
