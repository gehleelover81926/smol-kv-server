class Store:
    def __init__(self):
        self.data = {};

    def exists(self, key):
        return key in self.data

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def delete(self, key):
        return self.data.pop(key, None)
