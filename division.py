import pytest  

def divison(first_number,second_number):
    if second_number==0:
        return -1
    else:
        return first_number,second_number

def test_division():
    assert divison(5,0) == 0
    assert divison(5,1) == 5
