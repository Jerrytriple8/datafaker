"""Tests for datafaker generators."""
import unittest
import re
from datafaker import generators


class TestGenerators(unittest.TestCase):

    def test_first_name(self):
        name = generators.first_name()
        self.assertIsInstance(name, str)
        self.assertTrue(len(name) > 0)
        self.assertTrue(name[0].isupper())

    def test_last_name(self):
        name = generators.last_name()
        self.assertIsInstance(name, str)
        self.assertTrue(len(name) > 0)

    def test_full_name(self):
        name = generators.full_name()
        self.assertIn(" ", name)
        parts = name.split(" ")
        self.assertEqual(len(parts), 2)

    def test_email(self):
        email = generators.email()
        self.assertIn("@", email)
        self.assertGreater(len(email), 5)

    def test_email_custom_domain(self):
        email = generators.email(domain="test.com")
        self.assertTrue(email.endswith("@test.com"))

    def test_phone(self):
        phone = generators.phone()
        self.assertRegex(phone, r"\d{3}")

    def test_ipv4(self):
        ip = generators.ipv4()
        parts = ip.split(".")
        self.assertEqual(len(parts), 4)
        for p in parts:
            self.assertGreaterEqual(int(p), 1)
            self.assertLessEqual(int(p), 254)

    def test_ipv6(self):
        ip = generators.ipv6()
        parts = ip.split(":")
        self.assertEqual(len(parts), 8)

    def test_uuid_v4(self):
        u = generators.uuid_v4()
        self.assertRegex(u, r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")

    def test_date_val(self):
        d = generators.date_val()
        self.assertRegex(d, r"^\d{4}-\d{2}-\d{2}")

    def test_date_val_with_range(self):
        d = generators.date_val(start="2024-01-01", end="2024-12-31")
        self.assertTrue("2024" in d)

    def test_address(self):
        addr = generators.address()
        self.assertIn(",", addr)

    def test_record_default(self):
        rec = generators.record()
        self.assertIn("name", rec)
        self.assertIn("email", rec)
        self.assertIn("phone", rec)
        self.assertIn("address", rec)

    def test_record_custom_fields(self):
        rec = generators.record(fields=["ipv4", "uuid", "date"])
        self.assertIn("ipv4", rec)
        self.assertIn("uuid", rec)
        self.assertIn("date", rec)

    def test_integer(self):
        val = generators.integer(0, 100)
        self.assertGreaterEqual(val, 0)
        self.assertLessEqual(val, 100)

    def test_word(self):
        w = generators.word()
        self.assertIsInstance(w, str)
        self.assertTrue(len(w) > 0)


if __name__ == "__main__":
    unittest.main()
