from django.db import models
import datetime

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    summary = models.TextField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    logo = models.ImageField(upload_to='logos',blank=True)
    
    strand_choices = (
        ('ARC','Arch-OS'),
        ('BIO','Bio-OS'),
        ('DOM','Dome-OS'),
        ('ECO','Eco-OS'),
        ('SOC','S-OS'),
        ('OTH','Other'),
    )
    
    strand =  models.CharField(max_length=3,choices=strand_choices,blank=True)
    
    def __unicode__(self):
             return self.name
             
class Statistic(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
             return self.project.name + ": " + self.name + " " + self.value
             
class Link(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=100)
    url = models.URLField()
    
    type_choices = (
        ('SM','Social Media'),
        ('PC','Press Coverage'),
        ('PR','PR Release'),
        ('BP','Blog Post'),
        ('EV','Event'),
        ('DF','Data Feed'),
        ('OP','Output'),
    )
    
    type =  models.CharField(max_length=2,choices=type_choices,blank=True)
    
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
             return self.project.name + ": " + self.name
    
class File(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files')
    
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
             return self.project.name + ": " + self.name