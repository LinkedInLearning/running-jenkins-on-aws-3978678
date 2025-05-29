import json
import unittest
from unittest.mock import patch

from index import handler


class TestHandler(unittest.TestCase):
    # ------------------------------------------------------------------ #
    #  Test-harness set-up / tear-down
    # ------------------------------------------------------------------ #
    def setUp(self):
        # Supply deterministic values that the template injects
        self.mock_env = "test"
        self.env_patch = patch.dict(
            "os.environ",
            {
                "ENVIRONMENT": self.mock_env,
                "VERSION": "v0.0.0-test",
                "BUILD_TAG": "python3.12",
                "BUILD_NUMBER": "000",
            },
        )
        self.env_patch.start()

    def tearDown(self):
        self.env_patch.stop()

    # Convenience helper
    def _invoke(self, path):
        return handler(
            {
                "rawPath": path,
                "requestContext": {"http": {"method": "GET"}},
            },
            None,
        )

    # ------------------------------------------------------------------ #
    #  Docs page  (/)
    # ------------------------------------------------------------------ #
    def test_home_page_status_and_headers(self):
        resp = self._invoke("/")
        self.assertEqual(resp["statusCode"], 200)
        # Content-Type now includes charset
        self.assertEqual(resp["headers"]["Content-Type"], "text/html; charset=utf-8")

    def test_home_page_injects_environment(self):
        resp = self._invoke("/")
        # En-dash “–” is used in the <title>
        self.assertIn(f"The Python API – {self.mock_env}", resp["body"])

    # ------------------------------------------------------------------ #
    #  /data and /<id>
    # ------------------------------------------------------------------ #
    def test_get_all_data(self):
        with open("data.json", encoding="utf-8") as fh:
            expected = json.load(fh)

        resp = self._invoke("/data")
        self.assertEqual(resp["statusCode"], 200)
        self.assertEqual(resp["headers"]["Content-Type"], "application/json")
        self.assertEqual(json.loads(resp["body"]), expected)

    def test_get_item_by_id(self):
        with open("data.json", encoding="utf-8") as fh:
            data = json.load(fh)
        target_id = data[0]["id"]

        resp = self._invoke(f"/{target_id}")
        self.assertEqual(resp["statusCode"], 200)
        self.assertEqual(json.loads(resp["body"]), data[0])

    def test_invalid_id_returns_404(self):
        invalid_id = "does-not-exist"
        resp = self._invoke(f"/{invalid_id}")
        self.assertEqual(resp["statusCode"], 404)
        body = json.loads(resp["body"])
        # Error payload changed to: {"message": "item_id '<id>' not found"}
        self.assertEqual(body["message"], f"item_id '{invalid_id}' not found")


if __name__ == "__main__":
    unittest.main()
