from django.test import TestCase
from django.contrib.auth.models import User
from .models import Issue, IssueComments, IssueProject


class TestItemModel(TestCase):

    # testing Issue model

    def test_StatusAndResolutionDefaultsToCorrectValue(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password=None)

        issue = Issue(issueProjectName="Test Project", issueType="bug", title="Test title", affectsVersion="1.0.0", foundInBuild="1233", description="Test decription",
                    reporter=user)
        issue.save()

        self.assertEqual(issue.status, "Open")
        self.assertEqual(issue.resolution, "Unresolved")
    

    def test_NewIssueVotesDefaultsToCorrectValue(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password=None)

        issue = Issue(issueProjectName="Test Project", issueType="bug", title="Test title", affectsVersion="1.0.0", foundInBuild="1233", description="Test decription",
                    reporter=user)
        issue.save()

        # make sure by default number of votes is 0 for new issues
        self.assertEqual(issue.votes, 0)
    
    def test_IssueStrWorksCorrectly(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password=None)

        issue = Issue(issueProjectName="Test Project", issueType="bug", title="Test title", affectsVersion="1.0.0", foundInBuild="1233", description="Test decription",
                    reporter=user)
        issue.save()

        # make sure by default number of votes is 0 for new issues
        self.assertEqual(issue.__str__(), "{}-{}".format(issue.issueProjectName, issue.id))

    
    def test_CanCreateIssueOfTypeBug(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password=None)

        issue = Issue(issueProjectName="Test Project", issueType="bug", title="Test title", affectsVersion="1.0.0", foundInBuild="1233", description="Test decription",
                    reporter=user)
        issue.save()

        self.assertEqual(issue.issueType, "bug")
    
    def test_CanCreateIssueOfTypeFeature(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password=None)

        issue = Issue(issueProjectName="Test Project", issueType="feature_request", title="Test title", affectsVersion="1.0.0", foundInBuild="1233", description="Test decription",
                    reporter=user)
        issue.save()

        self.assertEqual(issue.issueType, "feature_request")
    

    def test_IssueReporterIsCorrect(self):
        # create 2 test users
        user1 = User.objects.create_user(username="test_user1", email=None, password=None)
        user2 = User.objects.create_user(username="test_user2", email=None, password=None)

        # create an issue using user1
        issue = Issue(issueProjectName="Test Project", issueType="feature_request", title="Test title", affectsVersion="1.0.0", foundInBuild="1233", description="Test decription",
                    reporter=user1)
        issue.save()
        self.assertEqual(issue.reporter, user1)


    # Testing IssueComments model

    def test_CommentShowsForCorrectIssue(self):
        # create a test user
        user = User.objects.create_user(username="test_user", email=None, password=None)

        # create 2 issues
        issue1 = Issue(issueProjectName="Test Project", issueType="feature_request", title="Test title 1", affectsVersion="1.0.0", foundInBuild="1233", description="Test decription",
                    reporter=user)
        issue1.save()

        issue2 = Issue(issueProjectName="Test Project", issueType="bug", title="Test title 2", affectsVersion="1.0.0", foundInBuild="1233", description="Test decription",
                    reporter=user)
        issue2.save()

        # create a comment for issue1
        comment = IssueComments(issueId=issue1, user=user, comment="Test comment")
        
        self.assertNotEqual(comment.issueId, issue2)
        self.assertEqual(comment.issueId, issue1)
    

    def test_CommentUserIsCorrect(self):
        # create 2 test users
        user1 = User.objects.create_user(username="test_user1", email=None, password=None)
        user2 = User.objects.create_user(username="test_user2", email=None, password=None)

        # create an issue using user1
        issue = Issue(issueProjectName="Test Project", issueType="feature_request", title="Test title", affectsVersion="1.0.0", foundInBuild="1233", description="Test decription",
                    reporter=user1)

        # create a comment for issue, using user1 as the 'user'
        comment = IssueComments(issueId=issue, user=user1, comment="Test comment")
        
        self.assertNotEqual(comment.user, user2)
        self.assertEqual(comment.user, user1)
    

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
