# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.template.context import RequestContext

from apps.project.models import Project, ShowcaseImage, ShowcaseCode, ProjectLog

def project_index(request):
    p_list = Project.objects.all().order_by('-weight') #orders by descending weight


    context = {'current_page':'project' , 'project_list':p_list}
    return render(request,'project/page/index.html' , context)

def project_main(request, project_url):
    project = get_object_or_404(Project, url=project_url)

    si_list = ShowcaseImage.objects.filter(project=project)
    sc_list = ShowcaseCode.objects.filter(project=project)
    pl_list = ProjectLog.objects.filter(project=project).order_by('timestamp')

    context = {'current_page':'project' , 'project': project, 'showcaseimage_list':si_list , 'showcasecode_list':sc_list , 'projectlog_list':pl_list}

    return render(request, 'project/page/main.html', context)