```python
import unittest
from src.code_generator import generateCode

class TestCodeGenerator(unittest.TestCase):

    def setUp(self):
        self.app_name = "TestApp"
        self.app_description = "This is a test app."

    def test_generateCode(self):
        code = generateCode(self.app_name, self.app_description)
        self.assertIsNotNone(code)

if __name__ == '__main__':
    unittest.main()
```