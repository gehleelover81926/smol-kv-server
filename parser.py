from store import Store

class CommandParser:
    def __init__(self, store: Store):
        self.store = store

        # THESE ARE COMMANDS SPECIFIC FOR THE STORE
        self.commands = ["SET", "DEL", "GET"]
    def execute(self, command: str):
        # SET username jynjo EX 20 - 5
        components = command.split(maxsplit=4)

        if not components:
            return "ERROR cannot process empty command"

        keyword = components[0].upper()
        key = ""

        # in cases where its a single word command, e.g (PING)
        if components[0] in self.commands:
            key = components[1]

        print(components)
        if keyword == "SET":
            if (len(components) < 3):
                return "ERROR expects 2 arguments (key, value)"

            # SET user jyn EX 60 (seconds)
            if "EX" in components:
                self.store.set_ttl(key, int(components[4]))

            self.store.set(key, components[2])

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
