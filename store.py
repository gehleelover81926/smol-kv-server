import time

class Store:
    def __init__(self):
        self.data = {};
        self.current_time = time.time(); # unix epoch timestamp

        # how this ttl works:
        #   key (same key stored in `data`): ttl (current_time + seconds)
        self.ttl = {};

    def set_ttl(self, key, ttl):
        total_ttl = self.current_time + ttl
        self.ttl[key] = total_ttl

    def get_ttl(self, key):
        # print(self.ttl)
        if key not in self.ttl:
            return None

        return self.ttl[key]

    def exists(self, key):
        return key in self.data

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        ttl = self.get_ttl(key)

        # not every key has a ttl
        if not ttl:
            return

        if  ttl >= time.time():
            return None

        print(ttl)
        return self.data.get(key)

    def delete(self, key):
        return self.data.pop(key, None)
