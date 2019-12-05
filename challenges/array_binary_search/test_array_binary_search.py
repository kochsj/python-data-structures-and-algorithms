from array_binary_search import binary_search

def test_zero_one_parameter():
    expected = -1
    actual = binary_search([4,8,15,16,23,42])
    assert expected == actual
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

def test_six_value_exists_short_list():
    expected = 0
    actual = binary_search([15], 15)
    assert expected == actual

def test_seven_value_exists_longer_list_at_mid():
    expected = 3
    actual = binary_search([4,8,15,16,23,42], 16)
    assert expected == actual   

def test_eight_value_exists_longer_list_not_at_mid():
    expected = 2
    actual = binary_search([4,8,15,16,23,42], 15)
    assert expected == actual

def test_nine_value_right_of_middle():
    expected = 4
    actual = binary_search([4,8,15,16,23,42], 23)
    assert expected == actual

def test_ten_value_right_of_middle_last_index():
    expected = 7
    actual = binary_search([4,8,15,16,23,42,55,90], 90)
    assert expected == actual

def test_eleven_value_left_of_middle_first_index():
    expected = 0
    actual = binary_search([4,8,15,16,23,42], 4)
    assert expected == actual

########################
# Stretch Goal
# ######################

def test_twelve_benchmark_list_length_100(benchmark):
    result = benchmark.pedantic(binary_search, kwargs={'lst': list(range(100)), 'value': 23}, iterations=1)
    assert result == 23

def test_thirteen_benchmark_list_length_1000(benchmark):
    result = benchmark.pedantic(binary_search, kwargs={'lst': list(range(1000)), 'value': 230}, iterations=1)
    assert result == 230 

def test_fourteen_benchmark_list_length_10000(benchmark):
    result = benchmark.pedantic(binary_search, kwargs={'lst': list(range(10000)), 'value': 2300}, iterations=1)
    assert result == 2300

def test_fifteen_benchmark_list_length_100000(benchmark):
    result = benchmark.pedantic(binary_search, kwargs={'lst': list(range(100000)), 'value': 23000}, iterations=1)
    assert result == 23000 