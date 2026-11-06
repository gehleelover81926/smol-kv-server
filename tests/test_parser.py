import unittest
from store import Store
from parser import CommandParser

class ParserTest(unittest.TestCase):

    def test_set_parser(self):
        store = Store()
        parser = CommandParser(store)

        command = "SET username gehlee"
        result = parser.execute(command)

        self.assertEqual(result, "OK")

    def test_get_parser(self):
        store = Store()
        parser = CommandParser(store)

        store.set("username", "gehlee")

        command = "GET username"
        result = parser.execute(command)

        self.assertEqual(result, "gehlee")

    def test_delete_parser(self):
        store = Store()
        parser = CommandParser(store)

        store.set("username", "gehlee")

        command = "DEL username"
        result = parser.execute(command)

        self.assertEqual(result, "1")

    def test_ping_parser(self):
        store = Store()
        parser = CommandParser(store)

        result = parser.execute("PING")

        self.assertEqual(result, "PONG")
