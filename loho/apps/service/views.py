# Create your views here.
from django.shortcuts import render
from django.template.loader import get_template
from django.template.context import RequestContext

def service_index(request):
    context = {'current_page':'service'}
    return render(request,'service/page/index.html',context)