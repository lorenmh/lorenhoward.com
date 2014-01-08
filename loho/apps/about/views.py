# Create your views here.
from django.shortcuts import render
from django.template.loader import get_template
from django.template.context import RequestContext
from django.shortcuts import render_to_response

from apps.about.models import Contact

import json

from django.http import HttpResponse

from apps.about.models import ContactForm

def about_index(request):
    contact_form = ContactForm()

    context = {'current_page':'about', 'contact_form': contact_form}
    return render(request,'about/page/index.html',context)

def contact_list(request):
    clist = list(Contact.objects.all())
    clist.reverse()

    context = {'contact_list': clist}
    return render_to_response('about/page/contact_list.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            mess = {"message":"success"}
            message = json.dumps(mess)

            return HttpResponse(status=201, content = message, content_type="application/json")
        else:
            errors = json.dumps(form.errors)
            return HttpResponse( status=409, content = errors, content_type="application/json") #REST, field error

