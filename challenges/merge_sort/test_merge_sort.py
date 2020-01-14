import pytest
from merge_sort import merge_sort

def test_merge_sort_simple():
    lst = [1,2,3,9,4,5]
    merge_sort(lst)
    assert lst == [1, 2, 3, 4, 5, 9]