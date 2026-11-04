import unittest
from store import Store

class TestScore(unittest.TestCase):
    def test_set_and_get(self):
        store = Store()

        store.set("name", "gehlee")

        self.assertEqual(store.get("name"), "gehlee")

    def test_get_nonexistent(self):
        store = Store()

        self.assertIsNone(store.get("nonexistent"))

    def test_delete(self):
        store = Store()

        store.set("delete", "this")
        store.delete("delete")

        self.assertFalse(store.exists("delete"));

    def test_delete_nonexistent(self):
        store = Store()

        store.delete("delete");
        self.assertFalse(store.exists("delete"));
