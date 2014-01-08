from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    website = models.URLField()
    subject = models.CharField(max_length=128)
    message = models.TextField()

    def __unicode__(self):
        return ("Name: %s, \t\t\t Email: %s" % (self.name, self.email))

class ContactForm(ModelForm):
    website = forms.URLField(required=False)
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'website','subject', 'message']

#The Page model will allow 'static' pages to be updated and altered.
#Boolean 'Publish' will only be allowed true for one object
class Page(models.Model):
    publish = models.BooleanField(default=False)