from django.test import TestCase
from .forms import IssueForm, IssueCommentsForm


class TestToDoItemForm(TestCase):

    # Issue Form Testing

    def test_CanCreateAnIssueWithAllIssueFieldsFilledIn(self):
        # all fields are filled in, so it should pass
        testDict = {"issueProjectName": "Test", "issueType": "bug", "title": "Test title", "affectsVersion": "1.0.0", 
        "foundInBuild": "123", "description": "Test description", "status": "Open", "resolution": "Unresolved"}

        form = IssueForm(testDict)

        self.assertTrue(form.is_valid())
    
    def test_MakeSureErrorIsThrownForMissingIssueFields(self):
        # 'title' field is missing, so it should fail
        testDict = {"issueProjectName": "Test", "issueType": "bug", "title": "", "affectsVersion": "1.0.0", 
        "foundInBuild": "123", "description": "Test description", "status": "Open", "resolution": "Unresolved"}

        form = IssueForm(testDict)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"], [u'This field is required.'])
    

    # Issue Comments Form Testing

    def test_CanCreateACommentWithCommentFieldFilledIn(self):
        testDict = {"comment": "Test comment"}

        form = IssueCommentsForm(testDict)

        self.assertTrue(form.is_valid())
    
    def test_MakeSureErrorIsThrownForMissingCommentField(self):
        # 'title' field is missing, so it should fail
        testDict = {"issueProjectName": "Test", "issueType": "bug", "title": "", "affectsVersion": "1.0.0", 
        "foundInBuild": "123", "description": "Test description", "status": "Open", "resolution": "Unresolved"}

        form = IssueCommentsForm(testDict)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["comment"], [u'This field is required.'])