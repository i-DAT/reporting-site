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

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'core.views.list_projects'),
    (r'^project/(?P<project_id>\d+)/$', 'core.views.display_project'),
    (r'^project/(?P<project_id>\d+)/edit/$', 'core.views.edit_project'),
    (r'^project/add/$', 'core.views.add_project'),
)
