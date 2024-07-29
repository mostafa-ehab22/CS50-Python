from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:00 PM to 10:50 AM") == "22:00 to 10:50"


def test_convert_ValueError():
    with pytest.raises(ValueError):
        convert("Mostafa Ehab doing CS50P")
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("15:00 AM to 25:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


