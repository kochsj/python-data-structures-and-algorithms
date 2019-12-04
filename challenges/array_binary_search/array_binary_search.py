def binary_search(lst=[], value=None):
    if value not in lst:
        return -1
    else:
        left_index = 0
        right_index = (len(lst) - 1)
        while left_index <= right_index:
            middle = (right_index + 1) // 2
            if value == lst[middle]:
                right_index = -1
                return lst[middle]
            elif value < lst[middle]:
                right_index = middle - 1
            else:
                left_index = middle + 1    