import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/1") == 100

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(60) == "60%"

def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")

def test_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
