import pytest
from bank import value, value_startswith

def test_hello_str():
    assert value("hello world!") == 0
    assert value("HeLlO") ==0

def test_hello_str_Startswith():
    assert value_startswith("hello world!") == 0

def test_h_not_hello():
    assert value("hasda asdasd") == 20
    assert value("Hasdakajhsd asd asd") == 20

def test_non_h_non_hello():
    assert value("fsehhh sakjh") == 100
    assert value(" hello") ==100

def test_empty_string():
    assert value("") ==100

def test_wrong():
    assert value_startswith("What's up as") ==0