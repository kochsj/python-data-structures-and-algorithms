from array_binary_search import binary_search

def test_one_value_not_in_list():
    expected = -1
    actual = binary_search([15], 9)
    assert expected == actual

def test_two_no_parameters():
    expected = -1
    actual = binary_search()
    assert expected == actual