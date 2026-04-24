import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from backend.service import get_project_name, get_health_status


class TestService(unittest.TestCase):

    def test_get_project_name(self):
        self.assertEqual(get_project_name(), "exp_test")

    def test_get_health_status_keys(self):
        result = get_health_status()
        self.assertIn("status", result)
        self.assertIn("project", result)

    def test_get_health_status_values(self):
        result = get_health_status()
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["project"], "exp_test")


if __name__ == "__main__":
    unittest.main()
