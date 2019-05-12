from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Issue, IssueComments
from projectManager.models import IssueProject


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
        numIssuesInitial = len(Issue.objects.all())

        # perform a post request and create a new issue using VALID data
        createNewIssueResponse = self.client.post("/bug-tracker/create/", {"issueProjectName": "Test", "issueType": "bug", "title": "TestTitle2019", "affectsVersion": "1.0.0", 
        "foundInBuild": "123", "description": "Test description"})

        # grab issue from db
        issue = get_object_or_404(Issue, pk=1)

        # grab the number of issues AFTER new issue has been created
        numIssuesFinal = len(Issue.objects.all())

        # verify that number of issues has changed, issue title is correct and after the issue is created, the page reloads back to the 'All Issues' page
        self.assertGreater(numIssuesFinal, numIssuesInitial)
        self.assertEqual(issue.title, "TestTitle2019")
        self.assertEqual(createNewIssueResponse.url, "/bug-tracker/")
    

    def test_CreatingANewIssueWithInvalidDataFails(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")
        
        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # grab the number of issues BEFORE creating a new issue
        numIssuesInitial = len(Issue.objects.all())

        # perform a post request with invalid data - title has been left blank
        createNewIssueResponse = self.client.post("/bug-tracker/create/", {"issueProjectName": "Test", "issueType": "bug", "title": "", "affectsVersion": "1.0.0", 
        "foundInBuild": "123", "description": "Test description"})

        # grab the number of issues AFTER new issue has been created
        numIssuesFinal = len(Issue.objects.all())

        # verify that number of issues has NOT changed
        self.assertEqual(numIssuesFinal, numIssuesInitial)


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

        # attempt to grab the detailed issue page for the created issue
        page = self.client.get("/bug-tracker/view-issue/1/")
        
        # page should load fine
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

        # create a new comment instance for the created issue & save it to db
        comment = IssueComments(comment="Test comment", issueId=issue, user=user)
        comment.save()

        # grab the initial number of comments
        numCommentsIntial = len(IssueComments.objects.all())

        # make a post request using valid data
        addCommentResponse = self.client.post("/bug-tracker/view-issue/1/", {"comment": "test comment"})

        # grab the number of comments after making the post request
        numCommentsFinal = len(IssueComments.objects.all())

        # verify that the number of comments has changed
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

        # create a new comment instance for the created issue & save it to db
        comment = IssueComments(comment="Test comment", issueId=issue, user=user)
        comment.save()
        
        # grab the initial number of comments
        numCommentsIntial = len(IssueComments.objects.all())

        # make a post request using invalid form data - the comment value is empty
        addCommentResponse = self.client.post("/bug-tracker/view-issue/1/", {"comment": ""})

        # grab the number of comments after making the post request
        numCommentsFinal = len(IssueComments.objects.all())

        # verify that the number of comments hasn't changed i.e. the invalid post request didn't add the comment
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

        # get the detailed issue page for the created issue
        page = self.client.get("/bug-tracker/edit-issue/1/")

        # it should load fine
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


    def test_IssueGetsUpdatedFineAfterMakingAValidEdit(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create new issue and grab it's id
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user)
        issue.save()
        id = issue.id

        # post request to update the issue with a new 'title'
        response = self.client.post("/bug-tracker/edit-issue/{}/".format(id), {"issueProjectName": "Test", "issueType": "bug", "title": "A DIFFERENT TITLE", "affectsVersion": "1.0.0", 
        "foundInBuild": "123", "description": "Test description"})
        issue = get_object_or_404(Issue, pk=id)

        # the title should be changed
        self.assertEqual(issue.title, "A DIFFERENT TITLE")
    

    def test_IssueDoesNotUpdateAfterMakingInValidEdit(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create new issue and grab it's id
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user)
        issue.save()
        id = issue.id

        # make a post request using INVALID form data
        response = self.client.post("/bug-tracker/edit-issue/{}/".format(id), {"issueProjectName": "TestTestTestTestTestTestTestTestTestTestTestTestTestTest", "issueType": "bug", "title": "A DIFFERENT TITLE", "affectsVersion": "1.0.0", 
        "foundInBuild": "123", "description": "Test description"})
        issue = get_object_or_404(Issue, pk=id)

        # issue's title should remain unchanged
        self.assertEqual(issue.title, "Initial title")


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

        # make post request to up vote issue
        response = self.client.post("/bug-tracker/up-vote/{}/".format(id), {"comment": "Test up vote"})
        updatedIssue = get_object_or_404(Issue, pk=id)

        # verify that issues's votes is greater than 0
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

        # make post request to resolve issue as 'Fixed'
        response = self.client.post("/bug-tracker/resolve-issue/{}/".format(id), {"resolution": "Fixed", "comment": "Resolving as fixed"})
        updatedIssue = get_object_or_404(Issue, pk=id)

        # verify that the issue's status is now 'Resolved' and resolution is 'Fixed'
        self.assertEqual(response.url, "/bug-tracker/view-issue/1/")
        self.assertEqual(updatedIssue.status, "Resolved")
        self.assertEqual(updatedIssue.resolution, "Fixed")

    
    def test_IssueResolvingWithInvalidFormFails(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create new issue and grab it's id
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user)
        issue.save()
        id = issue.id

        # post request with invalid form - Comments value is empty
        response = self.client.post("/bug-tracker/resolve-issue/{}/".format(id), {"resolution": "Fixed", "comment": ""})
        updatedIssue = get_object_or_404(Issue, pk=id)

        self.assertEqual(updatedIssue.status, "Open")
        self.assertEqual(updatedIssue.resolution, "Unresolved")


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
        
        # make post request to close issue
        response = self.client.post("/bug-tracker/close-issue/{}/".format(id), {"comment": "Closing"})
        updatedIssue = get_object_or_404(Issue, pk=id)

        # check that you get re-directed to the view issue page & the issue's status is now 'Closed'
        self.assertEqual(response.url, "/bug-tracker/view-issue/1/")
        self.assertEqual(updatedIssue.status, "Closed")

    
    def test_IssueClosingWithInvalidFormFails(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create new issue and grab it's id
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user, resolution="Fixed")
        issue.save()
        id = issue.id

        # post request with invalid form - Comments value is empty
        response = self.client.post("/bug-tracker/close-issue/{}/".format(id), {"comment": ""})
        updatedIssue = get_object_or_404(Issue, pk=id)

        # issue should remain Open
        self.assertEqual(updatedIssue.status, "Open")


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

        # make post request to re-open issue
        response = self.client.post("/bug-tracker/reopen-issue/{}/".format(id), {"comment": "Reopening"})
        updatedIssue = get_object_or_404(Issue, pk=id)

        # check that you get re-directed to the view issue page & the issue's status is now 'Re-Opened'
        self.assertEqual(response.url, "/bug-tracker/view-issue/1/")
        self.assertEqual(updatedIssue.status, "Re-Opened")
    

    def test_IssueReOpeningWithInvalidFormFails(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password="test")

        # login with user
        loginResponse = self.client.post("/accounts/login/", {"username": "test_user", "password": "test"})

        # create new issue and grab it's id
        issue = Issue(issueProjectName="Test", issueType="bug", title="Initial title", affectsVersion="1.0.0", 
        foundInBuild="123", description="Test description", reporter=user, resolution="Fixed", status="Closed")
        issue.save()
        id = issue.id

        # post request with invalid form - Comments value is empty
        response = self.client.post("/bug-tracker/reopen-issue/{}/".format(id), {"comment": ""})
        updatedIssue = get_object_or_404(Issue, pk=id)

        # Issue should remain 'Closed
        self.assertEqual(updatedIssue.status, "Closed")
    

    
