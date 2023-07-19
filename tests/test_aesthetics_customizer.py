```python
import unittest
from src.aesthetics_customizer import customizeAesthetics

class TestAestheticsCustomizer(unittest.TestCase):

    def setUp(self):
        self.app_details = {
            'app_name': 'Test App',
            'app_description': 'This is a test app'
        }

    def test_customize_aesthetics(self):
        result = customizeAesthetics(self.app_details)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
```