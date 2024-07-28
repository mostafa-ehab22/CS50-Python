from numb3rs import validate

def test_validate():

    assert validate("255.249.199.99") == True
    assert validate("0.9.19.50") == True

    assert validate("0.10.11.260") == False
    assert validate("0000.2222.1000.300") == False
