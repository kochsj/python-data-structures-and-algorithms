def merge_sort(list_of_ints):
    """
    Function that accepts a list of integers as an arguement
    Sorts the integers in place by value using a merge-sort algorithm; low to high
    No return; sorts the list 'in-place'
    """
    
    if len(list_of_ints) > 1: # list is more than one element(for sorting)

        middle_index = len(list_of_ints)//2
        left_slice = list_of_ints[:middle_index] # left half
        right_slice = list_of_ints[middle_index:] # right half

        merge_sort(left_slice) # recursion down to 1 element

        merge_sort(right_slice) # recursion down to 1 element

        _merge(left_slice, right_slice, list_of_ints) # helper function to merge left and right

def _merge(left, right, lst):
    """Responsible for merging a sorted right list of ints and sorted left list of ints together into one list"""
    i, j, k = 0,0,0

    while i < len(left) and j < len(right): # Assigns values of the final list starting at index 0 (k) the values of the lesser between left and right
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    if i == len(left): # you have exhausted all values in the left
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    else: # you have exhausted all values in right
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

