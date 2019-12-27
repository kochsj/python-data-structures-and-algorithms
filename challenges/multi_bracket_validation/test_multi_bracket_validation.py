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

def test_three_open_three_close():
    assert multi_bracket_validation('({[]})') == True

def test_open_with_no_close():
    assert multi_bracket_validation('({[]})(') == False

def test_all_open():
    assert multi_bracket_validation('({[') == False

def test_first_open_no_closing():
    assert multi_bracket_validation('(({[[()]]})') == False

def test_with_words():
    assert multi_bracket_validation('(abc[123{lmnop[hello_world(3)[4]]}])') == True

def test_fail_in_middle():
    assert multi_bracket_validation('({[(])})') == False
