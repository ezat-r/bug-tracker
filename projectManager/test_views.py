from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import IssueProject, IssueProject


class TestViews(TestCase):

    # Testing for no authentication handling - should reload to login page

    def test_ManageProjectsPageRedirectsToLoginPage(self):
        page = self.client.get("/manage-projects/view/")
        
        self.assertEqual(page.status_code, 302)
        self.assertEqual(page.url, "/accounts/login/?next=/manage-projects/view/")


    # Navigation with login

    def test_ManageProjectsPageLoadsFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with test user
        response = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        page = self.client.get("/manage-projects/view/")

        # should load fine and correct template should be used
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "project-manager/view-projects.html")
    

    def test_AddProjectPageLoadsFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with test user
        response = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        page = self.client.get("/manage-projects/add/")

        # should load fine and correct template should be used
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "project-manager/add-project.html")
    

    # Adding projects

    def test_AddProjectWithValidDataWorksFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with test user
        response = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        page = self.client.get("/manage-projects/add/")

        addProjectResponse = self.client.post("/manage-projects/add/", {"projectName": "Test"})

        project = get_object_or_404(IssueProject, pk=1)

        # should redirect to 'Manage Projects' page and new project should be added fine
        self.assertEqual(addProjectResponse.status_code, 302)
        self.assertEqual(addProjectResponse.url, "/manage-projects/view/")
        self.assertEqual(project.projectName, "Test")
    

    def test_AddProjectWithInvalidDataDoesntAddProjectItem(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with test user
        response = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        page = self.client.get("/manage-projects/add/")

        addProjectResponse = self.client.post("/manage-projects/add/", {"projectName": "TestTestTestTestTestTestTestTestTestTestTestTestTest"})

        projectCount = len(IssueProject.objects.all())

        # should redirect to 'Manage Projects' page and new project should be added fine
        self.assertEqual(addProjectResponse.status_code, 302)
        self.assertEqual(projectCount, 0)


    # Edit Project testing
    
    
    def test_GetEditProjectPageForProjectThatDoesNotExist(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # attempt to access edit issue page for non-existant item
        page = self.client.get("/manage-projects/edit/1/")

        # verify that a 404 is returned
        self.assertEqual(page.status_code, 404)


    def test_GetEditProjectPageForProjectThatDoesExist(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # create a test project
        project = IssueProject(projectName="Test")
        project.save()

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # attempt to access edit issue page for project item
        page = self.client.get("/manage-projects/edit/1/")

        # verify that a page loads fine
        self.assertEqual(page.status_code, 200)
    

    def test_EditProjectWithValidFormDataWorksFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # create a test project
        project = IssueProject(projectName="Test")
        project.save()

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # make post request with new VALID projectName value
        updateProjectResponse = self.client.post("/manage-projects/edit/1/", {"projectName": "Test Changed"})
        updatedProject = get_object_or_404(IssueProject, id=1)

        # verify that a re-direct happens and the issue's projectName is updated
        self.assertEqual(updateProjectResponse.status_code, 302)
        self.assertEqual(updatedProject.projectName, "Test Changed")
    

    def test_EditProjectWithInValidFormDataFailsToUpdateProjectName(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # create a test project
        project = IssueProject(projectName="Test")
        project.save()

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # make post request with INVALID projectName value
        updateProjectResponse = self.client.post("/manage-projects/edit/1/", {"projectName": "TestTestTestTestTestTestTestTestTestTestTestTestTestTest"})
        updatedProject = get_object_or_404(IssueProject, id=1)

        # verify that a re-direct happens and the issue's projectName stays the same
        self.assertEqual(updateProjectResponse.status_code, 302)
        self.assertEqual(updatedProject.projectName, "Test")

    
    # Deleting a project

    def test_DeleteProjectWorksFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # create a test project
        project = IssueProject(projectName="Test")
        project.save()

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # access the delete project url
        deleteProjectResponse = self.client.get("/manage-projects/delete/1/")
        projectCount = len(IssueProject.objects.all())

        # verify that a re-direct happens and number of projects in DB is 0
        self.assertEqual(deleteProjectResponse.status_code, 302)
        self.assertEqual(projectCount, 0)

    