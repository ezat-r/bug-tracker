from django.test import TestCase
from .forms import IssueProject, IssueProjectForm


class TestToDoItemForm(TestCase):

    # Issue Project Form Testing

    def test_CanCreateAnIssueWithAllFieldsFilledIn(self):
        # all fields are filled in, so it should pass
        testDict = {"projectName": "Test"}

        form = IssueProjectForm(testDict)

        self.assertTrue(form.is_valid())
    
    def test_MakeSureErrorIsThrownForMissingIssueFields(self):
        # 'title' field is missing, so it should fail
        testDict = {}

        form = IssueProjectForm(testDict)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["projectName"], [u'This field is required.'])
    
