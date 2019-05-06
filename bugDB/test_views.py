from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Issue, IssueComments


class TestViews(TestCase):

    def test_HomePageDefaultsToLoginPageWhenNotLoggedIn(self):
        page = self.client.get("/")

        # status code should be 302 - when not logged in, it will redirect users to login page
        self.assertEqual(page.status_code, 302)
    
    def test_LoginPageLoadsFine(self):
        page = self.client.get("/accounts/login/")

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "accounts/login.html")
    
