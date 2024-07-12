from plates import is_valid

def test_min_2letters():
    assert is_valid("A2222") == False
    assert is_valid("AA") == True

def test_length():
    assert is_valid("HI") == True
    assert is_valid("MOSTAFA") == False

def test_num():
    assert is_valid("AAA222") == True
    assert is_valid("AA2220") == True
    assert is_valid("AA220A") == False
    assert is_valid("AA0222") == False

def test_punc():
    assert is_valid("AAA!!") == False
    assert is_valid("AAA2,A") == False
