from src.utils import to_upper, utc_to_central

def test_to_upper():
    assert "FOOBAR" == to_upper("foobar")

def test_utc1():
    assert utc_to_central() is not None
