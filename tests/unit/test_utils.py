from src.utils import to_upper, utc_to_central, to_lower

def test_to_upper():
    assert "FOOBAR" == to_upper("foobar")

def test_utc1():
    assert utc_to_central() is not None

def test_to_lower():
    assert "foobar" == to_lower("FooBar")

def test_to_lower2():
    assert "foobar" == to_lower("FOOBar")
