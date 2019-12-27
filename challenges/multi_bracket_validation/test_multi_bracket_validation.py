import pytest
from multi_bracket_validation import multi_bracket_validation

def test_null_string():
    assert multi_bracket_validation('') == True

def test_easy_open_close():
    assert multi_bracket_validation('()') == True

def test_fail_open_close():
    assert multi_bracket_validation('(]') == False
    assert multi_bracket_validation('(}') == False
    assert multi_bracket_validation('{]') == False
    assert multi_bracket_validation('{)') == False
    assert multi_bracket_validation('[)') == False
    assert multi_bracket_validation('[}') == False
