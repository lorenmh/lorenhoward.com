# Create your views here.
from django.shortcuts import render
from django.template.loader import get_template
from django.template.context import RequestContext

def article_index(request):
	context = {'current_page':'article'}
        return render(request,'article/page/index.html',context)
