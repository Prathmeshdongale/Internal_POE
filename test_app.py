import unittest
from app import app

class FlaskTest(unittest.TestCase):
    def test_homepage(self):
        client = app.test_client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")

if __name__ == "__main__":
    unittest.main()