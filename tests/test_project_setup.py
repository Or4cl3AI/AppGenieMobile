```python
import unittest
from src import project_setup

class TestProjectSetup(unittest.TestCase):

    def setUp(self):
        self.project_setup = project_setup.setupProject()

    def test_get_app_details(self):
        app_name, app_description = self.project_setup.getAppDetails()
        self.assertIsInstance(app_name, str)
        self.assertIsInstance(app_description, str)

    def test_setup_project(self):
        result = self.project_setup.setupProject()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```