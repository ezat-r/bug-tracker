from django.apps import apps
from django.test import TestCase
from .apps import ProjectmanagerConfig


class TestTodoConfig(TestCase):

    # App tests
    def test_app(self):
        print("App Tests")
        self.assertEqual("projectManager", ProjectmanagerConfig.name)
        self.assertEqual("projectManager", apps.get_app_config("projectManager").name)