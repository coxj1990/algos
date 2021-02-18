from src.containers.lru_cache import LruCache

def test_trivial():
    cache = LruCache(2)
    cache.set('foo', 1)
    cache.set('bar', 2)
    assert cache.size() == 2
    assert cache.get('foo') == 1
    assert cache.size() == 2

def test_nontrivial():
    cache = LruCache(2)
    cache.set('foo', 1)
    cache.set('bar', 2)
    cache.get('foo')
    cache.set('baz', 3)
    assert cache.size() == 2
    assert cache.get('foo') == 1
    assert cache.get('baz') == 3
    assert cache.get('bar') == -1
