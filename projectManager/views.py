from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import IssueProject
from .forms import IssueProjectForm

# view for showing all projects
@login_required
def viewProjects(request):

    projects = IssueProject.objects.all()

    return render(request, "project-manager/view-projects.html", {"projects": projects})

# View for creating new projects
@login_required
def createProject(request):

    # check if a post request is made
    if request.method == "POST":

        # create a new projectForm using POST data
        projectForm = IssueProjectForm(request.POST)

        # check if form is valid
        if projectForm.is_valid():

            # it's valid so save it
            projectForm.save()

            # give a success message and go back to the view projects page
            messages.success(request, "Project added successfully!")

            return redirect("view_projects")

        else:
            # form is not valid so send an error message and go back to view projects page
            messages.error(request, "Error: Unable to add Project!")

            return redirect("view_projects")
    else:
        # otherwise, return an empty form to view
        projectForm = IssueProjectForm()

        form = {"form": projectForm}
    
    return render(request, "project-manager/add-project.html", form)


# view for editing a project
@login_required
def editProject(request, id):
    # grab project by id
    project = get_object_or_404(IssueProject, pk=id)

    if request.method == "POST":
        # create a IssueProjectForm instance using post data
        updatedProject = IssueProjectForm(request.POST, instance=project)

        # check if data is valid
        if updatedProject.is_valid():
            # it's valid so go ahead and save
            updatedProject.save()

         # give a success message and go back to the view projects page
            messages.success(request, "Project updated successfully!")

            return redirect("view_projects")

        else:
            # form is not valid so send an error message and go back to view projects page
            messages.error(request, "Error: Unable to update Project!")

            return redirect("edit_project", id)
        

    return render(request, "project-manager/edit-project.html", {"form": IssueProjectForm(instance=project), "project": project})


# Handling the deleting of a project
@login_required
def deleteProject(request, id):
    # grab project instance
    project = get_object_or_404(IssueProject, pk=id)

    # go ahead & delete it from DB
    project.delete()

    # give a success message and go back to the view projects page
    messages.success(request, "Project deleted successfully!")
    
    return redirect("view_projects")