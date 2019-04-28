from django.apps import apps
from django.test import TestCase
from .apps import BugdbConfig


class TestTodoConfig(TestCase):

    # App tests
    def test_app(self):
        print("App Tests")
        self.assertEqual("bugDB", BugdbConfig.name)
        self.assertEqual("bugDB", apps.get_app_config("bugDB").name)