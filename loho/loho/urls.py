from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'loho.views.home', name='home'),
    # url(r'^loho/', include('loho.foo.urls')),

    url(r'^$', 'apps.main.views.homepage'),
                       
    url(r'^blog/$', 'apps.blog.views.blog_index'),
    url(r'^blog/(?P<blog_url>[-\w]+)/$', 'apps.blog.views.blog_main'),
                       
    url(r'^about/$', 'apps.about.views.about_index'),
    url(r'^contact/$', 'apps.about.views.contact'),

    url(r'^comment/blog/(?P<blog_id>\d+)/$', 'apps.comment.views.comment_blog'),
    url(r'^comment/blog/(?P<blog_url>[-\w]+)/list/$', 'apps.comment.views.comment_list'),

    url(r'^contact/list/$', 'apps.about.views.contact_list'),

    url(r'^services/$', 'apps.service.views.service_index'),

    url(r'^projects/$', 'apps.project.views.project_index'),    
    url(r'^projects/(?P<project_url>[-\w]+)/$', 'apps.project.views.project_main'),

    url(r'^tag/(?P<tag_url>[-\w]+)/$', 'apps.tag.views.tag_main'),  
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^comments/', include('django.contrib.comments.urls')),


    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': '/home/lorenmh/lorenhoward.com/loho/static'}),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': '/home/lorenmh/lorenhoward.com/loho/media'}),

    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/base/img/favicon.ico'), name='favicon.ico'),
)

#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)