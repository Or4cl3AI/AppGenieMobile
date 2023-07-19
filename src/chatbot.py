```python
from src.code_generator import generateCode
from src.project_setup import setupProject
from src.aesthetics_customizer import customizeAesthetics
from src.recommendation_engine import provideRecommendations
from src.android_developer import assistAndroidDevelopment

class ChatBot:
    def __init__(self):
        self.app_name = ""
        self.app_description = ""

    def getAppDetails(self):
        self.app_name = input("What would you like to name your app? ")
        self.app_description = input("Please describe your app in a few words. ")

    def handleUserInput(self, user_input):
        if user_input == "APP_DETAILS":
            self.getAppDetails()
        elif user_input == "GENERATE_CODE":
            generateCode(self.app_name, self.app_description)
        elif user_input == "SETUP_PROJECT":
            setupProject(self.app_name)
        elif user_input == "CUSTOMIZE_AESTHETICS":
            customizeAesthetics(self.app_name)
        elif user_input == "RECOMMENDATIONS":
            provideRecommendations(self.app_name, self.app_description)
        elif user_input == "ANDROID_DEVELOPMENT":
            assistAndroidDevelopment(self.app_name)

    def startChat(self):
        print("Welcome to AppGenie Mobile, your app development assistant!")
        while True:
            user_input = input("Please enter a command: ")
            self.handleUserInput(user_input)
```