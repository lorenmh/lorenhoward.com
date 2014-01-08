# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.template.context import RequestContext

from apps.tag.models import Tag

from itertools import chain

def tag_main(request, tag_url):
    tag = get_object_or_404(Tag, url=tag_url)

    b_list = tag.blog_set.all()
    p_list = tag.project_set.all()

    results = sorted(chain(b_list, p_list), key=lambda instance: instance.timestamp)

    results.reverse()

    context = {'tag':tag, 'generic_list' : results}

    return render(request, 'tag/page/main.html', context)