from django.conf.urls import url
from .views import *

# URLs specific to the 'projectManager' app

urlpatterns = [
    url(r'^$', viewProjects, name="view_projects"),
    url(r'^view/$', viewProjects, name="view_projects"),
    url(r'^add/$', createProject, name="add_project"),
    url(r'^edit/(?P<id>[0-9]+)/$', editProject, name="edit_project"),
    url(r'^delete/(?P<id>[0-9]+)/$', deleteProject, name="delete_project"),
]