from twttr import shorten

def test_alpha():
    assert shorten("Mostafa") == "Mstf"
    assert shorten("CS50 Python") == "CS50 Pythn"
    assert shorten("HELLO WORLD!!!") == "HLL WRLD!!!"
