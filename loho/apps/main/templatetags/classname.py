from django import template

register = template.Library()

@register.filter(name='classname')
def classname(obj):
    classname = obj.__class__.__name__
    return classname