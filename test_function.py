import pytest
from function import sum_list, is_prime, divide, reverse_string, contains

#sum_list test
def test_empty_list():
    assert sum_list([]) == 0

def test_1_list():
    assert sum_list([3]) == 3

def test_multi_e_list():
    assert sum_list([3,4,5,6,7]) == 25

def test_negative_e_list():
    assert sum_list([3,-4,6,-7,-22]) == -24

# is_prime test
def test_lessthan2():
    assert is_prime(0) == False
    assert is_prime(1) == False

def test_prime():
    assert is_prime(7) == True
    assert is_prime(13) == True
    assert is_prime(29) == True

def test_non_prime():
    assert is_prime(4) == False
    assert is_prime(9) == False
    assert is_prime(15) == False

#divide test
def test_divide_positive():
    assert divide(3,6) == 0.5
    assert divide(4,2) == 2
    assert divide(15,3) == 5
    assert divide(21,7) == 3

def test_negative_divide_positive():
    assert divide(-10,2) == -5
    assert divide(-5,4) == -1.25

def test_divide_one():
    assert divide(4,1) == 4

def test_divide_zero():
    with pytest.raises(ValueError,match="Cannot divide by zero"):
        divide(5,0)

#reverse_string test
def test_reverse_empty():
    assert reverse_string("") == ""

def test_1char():
    assert reverse_string("d") =="d"

def test_string():
    assert reverse_string("1234567abcdefg") == "gfedcba7654321"

def test_space_string():
    assert reverse_string("Phan Le Nguyen") == "neyugN eL nahP"
    assert reverse_string("Dai hoc  Mo   hcm") == "mch   oM  coh iaD"

# contain test
def test_contain():
    assert contains([1,2,3,4,5,'6','7'],5) == True

def test_non_contain():
    assert contains([2,4,6,8,10],3) == False

def test_emptyList():
    assert contains([],5) == False