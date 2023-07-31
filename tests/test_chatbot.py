import unittest
from src.chatbot import ChatBot

class TestChatBot(unittest.TestCase):

    def setUp(self):
        self.chatbot = ChatBot()

    def test_get_app_details(self):
        app_name, app_description = self.chatbot.getAppDetails()
        self.assertIsNotNone(app_name)
        self.assertIsNotNone(app_description)

    def test_generate_code(self):
        code = self.chatbot.generateCode()
        self.assertIsNotNone(code)

    def test_setup_project(self):
        project = self.chatbot.setupProject()
        self.assertIsNotNone(project)

    def test_customize_aesthetics(self):
        aesthetics = self.chatbot.customizeAesthetics()
        self.assertIsNotNone(aesthetics)

    def test_provide_recommendations(self):
        recommendations = self.chatbot.provideRecommendations()
        self.assertIsNotNone(recommendations)

    def test_assist_android_development(self):
        android_dev = self.chatbot.assistAndroidDevelopment()
        self.assertIsNotNone(android_dev)

if __name__ == '__main__':
    unittest.main()