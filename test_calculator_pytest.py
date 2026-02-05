from unit_test import square
import pytest  #imported pytest library
#this program check for pytest run python -m pytest
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
def test_negative(): 
    assert square(-3) == 9
    assert square(-2) == 4
def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cow")