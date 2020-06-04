class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def put(self, key, val):
        idx = hash(key) % self.size
        buckets = self.table[idx]
        found = False
        for idx, (k, v) in enumerate(buckets):
            if k == key:
                buckets[idx] = (key, val)
                found = True
        if not found:
            buckets.append((key, val))

    def get(self, key):
        idx = hash(key) % self.size
        buckets = self.table[idx]
        for k, v in buckets:
            if k == key:
                return v
        return -1
