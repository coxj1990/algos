# Space efficient, small probability of false positives
# Only 1% probably of false positive with ~10 bits per element

from hashlib import sha1, md5

class BloomFilter:

    def __init__(self, n_hashes, n_bits):
        self.bits = [False for _ in range(n_bits)]
        self.hashes = self.get_hashes(n_hashes)

    def get_hash(self, i):
        def my_hash(s):
            h1 = int(sha1(s).hexdigest(), 16)
            h2 = int(md5(s).hexdigest(), 16)
            return h1 + i * h2
        return my_hash

    def get_hashes(self, n_hashes):
        return [self.get_hash(i) for i in range(n_hashes)]

    def add(self, s):
        for h in self.hashes:
            self.bits[h(s) % len(self.bits)] = True

    def query(self, s):
        for h in self.hashes:
            if not self.bits[h(s) % len(self.bits)]:
                return False
        return True
