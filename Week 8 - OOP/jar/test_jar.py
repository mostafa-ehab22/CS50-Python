import pytest
from jar import Jar

def test_initial_state():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_invalid_cookie():
    jar = Jar(10)

    with pytest.raises(ValueError, match="Invalid Cookies Number"):
        jar.deposit(-1)


def test_string():
    jar = Jar(10)
    assert str(jar) == ""

    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(2)

    assert jar.size == 2

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)

    jar.withdraw(1)
    assert jar.size == 4
