from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reports.views.home', name='home'),
    # url(r'^reports/', include('reports.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    #Registration Module
    
    (r'^accounts/', include('registration.backends.default.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'core.views.list_projects'),
    (r'^project/(?P<project_id>\d+)/$', 'core.views.display_project'),
    (r'^project/(?P<project_id>\d+)/edit/$', 'core.views.edit_project'),
    
    (r'^project/(?P<project_id>\d+)/link/$', 'core.views.add_link'),
    (r'^project/(?P<project_id>\d+)/link/(?P<link_id>\d+)/delete/$', 'core.views.delete_link'),
    
    (r'^project/(?P<project_id>\d+)/file/$', 'core.views.add_file'),
    (r'^project/(?P<project_id>\d+)/file/(?P<file_id>\d+)/delete/$', 'core.views.delete_file'),
    
    (r'^project/(?P<project_id>\d+)/stat/$', 'core.views.add_stat'),
    (r'^project/(?P<project_id>\d+)/stat/(?P<stat_id>\d+)/delete/$', 'core.views.delete_stat'),
    
    (r'^project/add/$', 'core.views.add_project'),
)
