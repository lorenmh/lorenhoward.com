from django.utils.text import Truncator
from django import template
from functools import wraps
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe, SafeData

register = template.Library()

"""I'm assuming this is required for the @stringfilter for the truncate words
edit:yep it is
"""
def stringfilter(func):
    """
    Decorator for filters which should only receive unicode objects. The object
    passed as the first positional argument will be converted to a unicode
    object.
    """
    def _dec(*args, **kwargs):
        if args:
            args = list(args)
            args[0] = force_text(args[0])
            if (isinstance(args[0], SafeData) and
                getattr(_dec._decorated_function, 'is_safe', False)):
                return mark_safe(func(*args, **kwargs))
        return func(*args, **kwargs)

    # Include a reference to the real function (used to check original
    # arguments by the template parser, and to bear the 'is_safe' attribute
    # when multiple decorators are applied).
    _dec._decorated_function = getattr(func, '_decorated_function', func)

    for attr in ('is_safe', 'needs_autoescape'):
        if hasattr(func, attr):
            import warnings
            warnings.warn("Setting the %s attribute of a template filter "
                          "function is deprecated; use @register.filter(%s=%s) "
                          "instead" % (attr, attr, getattr(func, attr)),
                          DeprecationWarning)
            setattr(_dec, attr, getattr(func, attr))

    return wraps(func)(_dec)

@register.filter(is_safe=True)
@stringfilter
def truncatewords_html_special(value, arg):

    """
    Assumes that the first argument is the length, and the second is the URL
    """

    length = arg

    endtext = ' ...'

    try:
        length = int(length)
    except ValueError: # invalid literal for int()
        return value # Fail silently.
    return Truncator(value).words(length, html=True, truncate=endtext)