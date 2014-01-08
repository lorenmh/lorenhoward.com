# Create your views here.
from django.shortcuts import render
from django.template.loader import get_template
from django.template.context import RequestContext

from apps.project.models import Project
from apps.blog.models import Blog

from itertools import chain

def homepage(request):
    def get_browser():
        try:
            browser = request.META['HTTP_USER_AGENT']
        except KeyError:
            browser = 'Unknown'
        return browser

    context = {'browser':get_browser()}

    b_list = Blog.objects.filter(publish = True)
    p_list = Project.objects.filter(publish = True)

    #reverse = True will put newer items
    results = sorted(chain(b_list, p_list), key=lambda instance: instance.timestamp)

    results.reverse()

    context = {'browser':get_browser(), 'generic_list':results}

    return render(request, 'homepage.html', context)
