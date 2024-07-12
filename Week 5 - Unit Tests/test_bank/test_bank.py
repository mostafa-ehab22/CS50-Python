from bank import value

def test_value():
    assert value("hello") == 0
    assert value("HI") == 20
    assert value("A Truly BEAUTIFUL Afternoon") == 100