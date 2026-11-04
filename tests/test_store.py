import unittest
from store import Store

class TestScore(unittest.TestCase):
    def test_set_and_get(self):
        store = Store()

        store.set("name", "gehlee")

        self.assertEqual(store.get("name"), "gehlee")
