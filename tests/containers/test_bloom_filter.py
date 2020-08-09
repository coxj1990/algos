from src.containers.bloom_filter import BloomFilter

N_HASHES = 10
N_BITS = 1024

def test_trivial():
    bf = BloomFilter(N_HASHES, N_BITS)
    assert not bf.query('test')

def test_nontrivial():
    bf = BloomFilter(N_HASHES, N_BITS)
    bf.add('foo')
    assert bf.query('foo')
    assert not bf.query('bar')
    bf.add('bar')
    assert bf.query('bar')
