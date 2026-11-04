from store import Store

class CommandParser:
    def __init__(self, store: Store):
        self.store = store

    def execute(self, command: str):
        components = command.split(maxsplit=2)

        if not components:
            return "ERROR cannot process empty command"

        keyword = components[0].upper()

        if keyword == "SET":
            if (len(components) != 3):
                return "ERROR expects 2 arguments (key, value)"

            self.store.set(components[1], components[2])

            return "OK"

        elif keyword == "GET":
            if (len(components) != 2):
                return "ERROR expects 1 argument (key)"

            if not self.store.exists(components[1]):
                return "(nil)"

            value = self.store.get(components[1])
            return str(value)

        elif keyword == "DEL":
            if (len(components) != 2):
                return "ERROR expects 1 argument (key)"

            if not self.store.exists(components[1]):
                return "0"

            value = self.store.delete(components[1])
            return "1"

        elif keyword == "PING":
            if (len(components) != 1):
                return "ERROR wrong number of arguments"
            return "PONG"

        return "ERROR unknown command"
