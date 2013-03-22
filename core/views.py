from models import *

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.mail import EmailMessage
from django.db.models import Count
from django.utils import timezone

from django.forms import ModelForm

class ProjectForm(ModelForm):
    class Meta:
            model = Project

def list_projects(request):
    project_list = Project.objects.all()
    
    return render_to_response('list.html',{
               'project_list':project_list
           }, context_instance=RequestContext(request))
           
def display_project(request, project_id):
    the_project = get_object_or_404(Project, pk=project_id)
    stat_list = Statistic.objects.filter(project=the_project)
    link_list = Link.objects.filter(project=the_project)
    
    return render_to_response('single.html',{
               'project':the_project,
               'stat_list':stat_list,
               'link_list':link_list
           }, context_instance=RequestContext(request))
           
           
def add_project(request):
    #set clear values for Form data
    success = False
    
    if request.method == "POST":
        project_form = ProjectForm(request.POST, request.FILES)
        
        if project_form.is_valid():
            new_project = project_form.save()
            #new_project = project_form.save(commit=False)
            #new_project.logo = request.POST['logo']
            #new_project.save()
            
            return redirect('/')
    
    
    else:
        project_form = ProjectForm()
    
    return render_to_response('add.html',{
               'project_form':project_form
           }, context_instance=RequestContext(request))
           
    
def edit_project(request, project_id):
    #set clear values for Form data
    #success = False
    the_project = get_object_or_404(Project, pk=project_id)
    
    
    if request.method == "POST":
        project_form = ProjectForm(request.POST, request.FILES, instance=the_project)
        
        if project_form.is_valid():
            the_project = project_form.save()
            #new_project = project_form.save(commit=False)
            #new_project.logo = request.POST['logo']
            #new_project.save()
            
            return redirect('/project/'+ project_id +'/')
    
    
    else:
        project_form = ProjectForm(instance=the_project)
    
    return render_to_response('add.html',{
               'project_form':project_form
           }, context_instance=RequestContext(request))
