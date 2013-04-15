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

from django import forms
from django.forms import ModelForm

class ProjectForm(ModelForm):
    class Meta:
            model = Project
            
class AddFileForm(forms.Form):
    file_name = forms.CharField(max_length=100)
    file  = forms.FileField()
    
class AddLinkForm(forms.Form):
    name = forms.CharField(max_length=100)
    url = forms.URLField()
    
    type_choices = (
        ('SM','Social Media'),
        ('PC','Press Coverage'),
        ('PR','PR Release'),
        ('BP','Blog Post'),
        ('EV','Event'),
        ('DF','Data Feed'),
        ('OP','Output'),
        ('OT','Other'),
    )
    
    type =  forms.ChoiceField(choices=type_choices)
    
class AddStatForm(forms.Form):
    name = forms.CharField(max_length=100)
    value = forms.CharField(max_length=100)
    
    
def add_file(request, project_id):
    the_project = get_object_or_404(Project, pk=project_id)
    success = False
    
    if request.method == "POST": 
        file_form = AddFileForm(request.POST, request.FILES)
        
        if file_form.is_valid():
            success = True
            
            file_obj = File()
            file_obj.project = the_project
            file_obj.file = request.FILES['file']
            file_obj.name = file_form.cleaned_data['file_name']
            
            file_obj.save()
            
            return redirect('/project/'+ project_id +'/')
            
    else:
        file_form = AddFileForm()
    
    return render_to_response('add_elements/file.html',{
               'project_id':project_id,
               'file_form':file_form,
           }, context_instance=RequestContext(request))

def add_link(request, project_id):
    the_project = get_object_or_404(Project, pk=project_id)
    success = False
    
    if request.method == "POST":
        link_form = AddLinkForm(request.POST)
        
        if link_form.is_valid():
	        success = True
	        
	        link_obj = Link()
	        link_obj.project = the_project
	        link_obj.name = link_form.cleaned_data['name']
	        link_obj.url = link_form.cleaned_data['url']
	        link_obj.type = link_form.cleaned_data['type']
	        link_obj.save()
	        return redirect('/project/'+ project_id +'/')
	        
    else:
        link_form = AddLinkForm
        
    return render_to_response('add_elements/link.html',{
               'project_id':project_id,
               'link_form':link_form,
           }, context_instance=RequestContext(request))

def add_stat(request, project_id):
    the_project = get_object_or_404(Project, pk=project_id)
    success = False
    
    if request.method == "POST":
        stat_form = AddStatForm(request.POST)
        
        if stat_form.is_valid():
	        success = True
	        
	        stat_obj = Statistic()
	        stat_obj.project = the_project
	        stat_obj.name = stat_form.cleaned_data['name']
	        stat_obj.value = stat_form.cleaned_data['value']
	        stat_obj.save()
	        return redirect('/project/'+ project_id +'/')
	        
    else:
        stat_form = AddStatForm
        
    return render_to_response('add_elements/stat.html',{
               'project_id':project_id,
               'stat_form':stat_form,
           }, context_instance=RequestContext(request))

def list_projects(request):
    project_list = Project.objects.all()
    
    return render_to_response('list.html',{
               'project_list':project_list
           }, context_instance=RequestContext(request))
           
def display_project(request, project_id):
    the_project = get_object_or_404(Project, pk=project_id)
    stat_list = Statistic.objects.filter(project=the_project)
    link_list = Link.objects.filter(project=the_project)
    file_list = File.objects.filter(project=the_project)
    
    return render_to_response('single.html',{
               'project':the_project,
               'stat_list':stat_list,
               'link_list':link_list,
               'file_list':file_list
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
