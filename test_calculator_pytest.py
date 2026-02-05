from unit_test import square
#this program check for pytest run python -m pytest
def test_square():
    assert square(2) == 4
    assert square(3) == 9 
    assert square(-3) == 9
    assert square(-2) == 4
