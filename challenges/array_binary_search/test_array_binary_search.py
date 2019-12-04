from array_binary_search import binary_search

def test_one_no_parameters():
    expected = -1
    actual = binary_search()
    assert expected == actual

def test_two_value_not_in_short_list():
    expected = -1
    actual = binary_search([15], 9)
    assert expected == actual

def test_three_value_not_in_longer_list():
    expected = -1
    actual = binary_search([4,8,15,16,23,42], 90)
    assert expected == actual

def test_four_value_not_in_mixed_type_list():
    expected = -1
    actual = binary_search(['apple', 14, True, 'Thor', None], 90)
    assert expected == actual

def test_five_non_integer_value():
    expected = -1
    actual = binary_search([4,8,15,16,23,42], 'apple')
    assert expected == actual