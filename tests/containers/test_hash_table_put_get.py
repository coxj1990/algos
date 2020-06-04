from src.containers.hash_table_put_get import HashTable

def test_trivial_found():
    t = HashTable(1)
    t.put("test", 0)
    assert t.get("test") == 0

def test_trivial_not_found():
    t = HashTable(1)
    t.put("test", 0)
    assert t.get("foo") == -1

def test_replace():
    t = HashTable(1)
    t.put("test", 0)
    t.put("test", 1)
    assert t.get("test") == 1

def test_nontrivial():
    t = HashTable(2)
    t.put("foo", 0)
    t.put("bar", 1)
    t.put("foobar", 2)
    assert t.get("foobar") == 2
