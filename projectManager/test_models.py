from django.test import TestCase
from django.contrib.auth.models import User
from .models import IssueProject


class TestItemModel(TestCase):

    # Testing IssueProject Model

    def test_CanCreateNewProject(self):
        # create a test project
        newProjectName = "Test"

        newProject = IssueProject(projectName=newProjectName)

        self.assertEqual(newProject.projectName, newProjectName)


    def test_ProjectStrWorksCorrectly(self):
        # create a test project
        newProjectName = "Test"

        newProject = IssueProject(projectName=newProjectName)
        
        self.assertEqual(newProject.__str__(), newProjectName)
