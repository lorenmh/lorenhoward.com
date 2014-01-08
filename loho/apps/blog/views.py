# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.loader import get_template
from django.template.context import RequestContext

from django.contrib.contenttypes.models import ContentType

from apps.blog.models import Blog
from apps.comment.models import Comment, CommentForm


page_context = {'current_page':'blog'}

def blog_index(request):
    blog_list = list(Blog.objects.all().order_by('-timestamp'))

    current_context = {'blog_list':blog_list}
    context = dict(page_context.items() + current_context.items())

    return render(request,'blog/page/index.html',context)

def comment_list(request, blog_id):
    ct = ContentType.objects.get(app_label='blog', model='blog')
    blog = get_object_or_404(Blog, id = blog_id)
    clist = Comment.objects.filter(object_id = blog.id, content_type=ct)

    #make sure to add the URLs and the comment_list.html file
    context = {'comment_list': clist}
    return render_to_response('comment/component/comment_list.html', context)

def blog_main(request, blog_url):
    blog = get_object_or_404(Blog, url=blog_url)
    comment_form = CommentForm()

    ct = ContentType.objects.get(app_label='blog', model='blog')
    clist = Comment.objects.filter(object_id = blog.id, content_type=ct)

    current_context = {'blog':blog, 'comment_form':comment_form, 'comment_list':clist}

    context = dict(page_context.items() + current_context.items())
    
    return render(request, 'blog/page/main.html', context)
