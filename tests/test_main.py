import unittest
from src import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app_name = "Test App"
        self.app_description = "This is a test app"

    def test_getAppDetails(self):
        app_details = main.getAppDetails(self.app_name, self.app_description)
        self.assertEqual(app_details['name'], self.app_name)
        self.assertEqual(app_details['description'], self.app_description)

    def test_generateCode(self):
        code = main.generateCode(self.app_name, self.app_description)
        self.assertIsNotNone(code)

    def test_setupProject(self):
        project_setup_status = main.setupProject(self.app_name)
        self.assertTrue(project_setup_status)

    def test_customizeAesthetics(self):
        aesthetics_status = main.customizeAesthetics(self.app_name)
        self.assertTrue(aesthetics_status)

    def test_provideRecommendations(self):
        recommendations = main.provideRecommendations(self.app_name, self.app_description)
        self.assertIsNotNone(recommendations)

    def test_assistAndroidDevelopment(self):
        android_dev_status = main.assistAndroidDevelopment(self.app_name)
        self.assertTrue(android_dev_status)

if __name__ == '__main__':
    unittest.main()