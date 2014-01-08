# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.loader import get_template
from django.template.context import RequestContext

from django.http import HttpResponse

from django.contrib.contenttypes.models import ContentType
import json

from apps.blog.models import Blog
from apps.comment.models import Comment, CommentForm

page_context = {'current_page':'blog'}

def comment_blog(request, blog_id):
    if (Blog.objects.get(pk = blog_id)):
        if request.method == 'POST':

            ct = ContentType.objects.get(app_label='blog', model='blog')

            form = CommentForm(request.POST, content_type=ct, object_id=blog_id)

            if form.is_valid():
                form.save()
                mess = {"message":"success"}
                message = json.dumps(mess)

                return HttpResponse(status=201, content = message, content_type="application/json")
            else:
                errors = json.dumps(form.errors)
                return HttpResponse( status=409, content = errors, content_type="application/json") #REST, field error

def comment_list(request, blog_url):
    ct = ContentType.objects.get(app_label='blog', model='blog')
    blog = get_object_or_404(Blog, url = blog_url)
    clist = Comment.objects.filter(object_id = blog.id, content_type=ct)

    #make sure to add the URLs and the comment_list.html file
    context = {'comment_list': clist}
    return render_to_response('comment/component/comment_list.html', context)