from seasons import valid_date_format

def test_valid_date_format():
    assert valid_date_format("2003-02-20") == True
    assert valid_date_format("1990-2-25") == False
    assert valid_date_format("January, 1 2007") == False
