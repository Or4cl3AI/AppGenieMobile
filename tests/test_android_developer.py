```python
import unittest
from src.android_developer import AndroidDeveloper

class TestAndroidDeveloper(unittest.TestCase):

    def setUp(self):
        self.android_dev = AndroidDeveloper()

    def test_assist_android_development(self):
        app_name = "TestApp"
        app_description = "This is a test app"
        self.android_dev.assistAndroidDevelopment(app_name, app_description)
        self.assertIsNotNone(self.android_dev.app_details)

if __name__ == '__main__':
    unittest.main()
```