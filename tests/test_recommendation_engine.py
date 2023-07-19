```python
import unittest
from src.recommendation_engine import RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):

    def setUp(self):
        self.recommendation_engine = RecommendationEngine()

    def test_provide_recommendations(self):
        app_details = {"app_name": "Test App", "app_description": "This is a test app"}
        recommendations = self.recommendation_engine.provide_recommendations(app_details)
        self.assertIsInstance(recommendations, list)

if __name__ == '__main__':
    unittest.main()
```