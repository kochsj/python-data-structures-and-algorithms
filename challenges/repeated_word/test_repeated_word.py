import pytest
from repeated_word import repeated_word

def test_simple_string():
    string = "Once upon a time, there was a brave princess who.."
    lst = repeated_word(string)
    assert lst[0] == 'a'