from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Issue, IssueComments, IssueProject


class TestViews(TestCase):

    # Testing for no authentication handling - should reload to login page

    def test_LoginPageLoadsFine(self):
        page = self.client.get("/accounts/login/")

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "accounts/login.html")


    def test_AllIssuesPageDefaultsToLoginPageWhenNotLoggedIn(self):
        page = self.client.get("/")

        # status code should be 302 - when not logged in, it will redirect users to login page
        self.assertEqual(page.status_code, 302)
        self.assertEqual(page.url, "/accounts/login/")


    def test_DetailedIssueViewPageRedirectsToLoginPageWhenNotLoggedIn(self):

        page = self.client.get("/bug-tracker/view-issue/1/")
        
        # status code should be 302 - when not logged in, it will redirect users to login page
        self.assertEqual(page.status_code, 302)
        self.assertEqual(page.url, "/accounts/login/?next=/bug-tracker/view-issue/1/")


    def test_CreateNewIssuePageRedirectsToLoginPageWhenNotLoggedIn(self):
        page = self.client.get("/bug-tracker/create/")
        
        # status code should be 302 - when not logged in, it will redirect users to login page
        self.assertEqual(page.status_code, 302)
        self.assertEqual(page.url, "/accounts/login/")
    

    def test_EditIssuePageRedirectsToLoginPageWhenNotLoggedIn(self):
        page = self.client.get("/bug-tracker/edit-issue/1/")
        
        # status code should be 302 - when not logged in, it will redirect users to login page
        self.assertEqual(page.status_code, 302)
        self.assertEqual(page.url, "/accounts/login/")


    # Tests for navigating to pages with valid & invalid authentication

    def test_InvalidLoginReloadsLoginPage(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with wrong Username & Password
        response = self.client.post("/accounts/login/", {"username": "test", "password": "wrongpass"})

        # should reload to Login page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")


    def test_RedirectedToAnalyticsPageAfterAUserLogin(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with correct Username & Password
        response = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # should be redirected to the 'Issue Analytics' page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/bug-tracker/analytics/")

    
    def test_AnalyticsPageLoadsFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with correct Username & Password
        response = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        project = IssueProject(projectName="Project_Name")
        project.save()

        # create a new issue
        issue = Issue(issueProjectName="Project_Name", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user)
        issue.save()

        page = self.client.get("/bug-tracker/analytics/")

        # should be redirected to the 'Issue Analytics' page
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bug-tracker/issue-analytics.html")

    
    def test_AllIssuesPageLoadsFineAfterLogin(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with correct Username & Password
        response = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        page = self.client.get("/bug-tracker/")

        # verify page loads fine
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bug-tracker/all-issues.html")
    

    # Create new Issue view testing

    def test_CreateNewIssuePageLoadsFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        response = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        page = self.client.get("/bug-tracker/create/")

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bug-tracker/create-new-issue.html")


    def test_CreatingANewIssueWorksFineAndReloadsToAllIssuesPage(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # grab the number of issues BEFORE creating a new issue
        allIssuesInitial = Issue.objects.all()
        numIssuesInitial = len(allIssuesInitial)

        # perform a post request and create a new issue
        createNewIssueResponse = self.client.post("/bug-tracker/create/", {"issueProjectName": "Test", "issueType": "bug", "title": "TestTitle2019", "affectsVersion": "1.0.0", 
        "foundInBuild": "123", "description": "Test description"})

        # grab issue from db
        issue = get_object_or_404(Issue, pk=1)

        # grab the number of issues AFTER new issue has been created
        allIssuesFinal = Issue.objects.all()
        numIssuesFinal = len(allIssuesFinal)

        # verify that number of issues has risen, issue title is correct and after the issue is created reload back to the 'All Issues' page
        self.assertGreater(numIssuesFinal, numIssuesInitial)
        self.assertEqual(issue.title, "TestTitle2019")
        self.assertEqual(createNewIssueResponse.url, "/bug-tracker/")


    ## Detailed issue view testing

    # test for issue that DOESN'T exist
    def test_GetDetailedIssuePageForIssueThatDoesNotExist(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # attempt to access edit issue page for non-existant item
        page = self.client.get("/bug-tracker/view-issue/1/")

        # verify that a 404 is returned
        self.assertEqual(page.status_code, 404)


    # test for issue that DOES exist
    def test_GetDetailedIssuePageForAnIssueThatDoesExist(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create a new issue
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user)
        issue.save()

        page = self.client.get("/bug-tracker/view-issue/1/")
        
        # status code should be 302 - when not logged in, it will redirect users to login page
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bug-tracker/bug-detailed-view.html")

    # test for adding a new comment against issue
    def test_AddingNewCommentWorksFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create a new issue
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user)
        issue.save()

        comment = IssueComments(comment="Test comment", issueId=issue, user=user)
        comment.save()

        numCommentsIntial = len(IssueComments.objects.all())

        addCommentResponse = self.client.post("/bug-tracker/view-issue/1/", {"comment": "test comment"})

        numCommentsFinal = len(IssueComments.objects.all())

        self.assertGreater(numCommentsFinal, numCommentsIntial)

    
    def test_AddingAnInvalidCommentDoesntGetAdded(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create a new issue
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user)
        issue.save()

        comment = IssueComments(comment="Test comment", issueId=issue, user=user)
        comment.save()

        numCommentsIntial = len(IssueComments.objects.all())

        addCommentResponse = self.client.post("/bug-tracker/view-issue/1/", {"commen": "test comment"})

        numCommentsFinal = len(IssueComments.objects.all())

        self.assertEqual(numCommentsFinal, numCommentsIntial)


    # Edit issue view testing

    def test_EditIssuePageLoadsFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create new issue
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user)
        issue.save()

        page = self.client.get("/bug-tracker/edit-issue/1/")

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bug-tracker/edit-issue.html")


    def test_GetEditIssuePageForItemThatDoesNotExist(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # attempt to access edit issue page for non-existant item
        page = self.client.get("/bug-tracker/edit-issue/1/")

        # verify that a 404 is returned
        self.assertEqual(page.status_code, 404)


    def test_IssueGetsUpdatedFineAfterMakingAnEdit(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create new issue and grab it's id
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user)
        issue.save()
        id = issue.id

        response = self.client.post("/bug-tracker/edit-issue/{}/".format(id), {"issueProjectName": "Test", "issueType": "bug", "title": "A DIFFERENT TITLE", "affectsVersion": "1.0.0", 
        "foundInBuild": "123", "description": "Test description"})
        issue = get_object_or_404(Issue, pk=id)

        self.assertEqual(issue.title, "A DIFFERENT TITLE")


    ## Upvoting issue view testing

    def test_IssueUpvotingWorksFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create new issue and grab it's id
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user)
        issue.save()
        id = issue.id

        response = self.client.post("/bug-tracker/up-vote/{}/".format(id), {"comment": "Test up vote"})
        updatedIssue = get_object_or_404(Issue, pk=id)

        self.assertEqual(response.url, "/bug-tracker/view-issue/1/")
        self.assertGreater(updatedIssue.votes, 0)


    ## Resolving issue view testing

    def test_IssueResolvingWorksFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create new issue and grab it's id
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user)
        issue.save()
        id = issue.id

        response = self.client.post("/bug-tracker/resolve-issue/{}/".format(id), {"resolution": "Fixed", "comment": "Resolving as fixed"})
        updatedIssue = get_object_or_404(Issue, pk=id)

        self.assertEqual(response.url, "/bug-tracker/view-issue/1/")
        self.assertEqual(updatedIssue.status, "Resolved")
        self.assertEqual(updatedIssue.resolution, "Fixed")


    ## Closing issue view testing

    def test_IssueClosingWorksFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create new issue and grab it's id
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user, resolution="Fixed")
        issue.save()
        id = issue.id

        response = self.client.post("/bug-tracker/close-issue/{}/".format(id), {"comment": "Closing"})
        updatedIssue = get_object_or_404(Issue, pk=id)

        self.assertEqual(response.url, "/bug-tracker/view-issue/1/")
        self.assertEqual(updatedIssue.status, "Closed")


    ## Re-opening view issue testing

    def test_IssueReOpeningWorksFine(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create new issue and grab it's id
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user, resolution="Fixed", status="Closed")
        issue.save()
        id = issue.id

        response = self.client.post("/bug-tracker/reopen-issue/{}/".format(id), {"comment": "Reopening"})
        updatedIssue = get_object_or_404(Issue, pk=id)

        self.assertEqual(response.url, "/bug-tracker/view-issue/1/")
        self.assertEqual(updatedIssue.status, "Re-Opened")


    # def test_get_edit_item_page(self):
    #     item = Item(name="Create a Test")
    #     item.save()

    #     page = self.client.get("/edit/{0}".format(item.id))
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "item_form.html")
    
