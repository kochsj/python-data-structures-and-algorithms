def quick_sort(arr, left_index, right_index):
    if left_index < right_index:
        # Partition the array by setting the position of the pivot value 
        position = partition(arr, left_index, right_index)
        # Sort the left_index
        quick_sort(arr, left_index, position - 1)
        # Sort the right_index
        quick_sort(arr, position + 1, right_index)

def partition(arr, left_index, right_index):
    # set a pivot value as a point of reference
    pivot = arr[right_index]

    # create a variable to track the largest index of numbers lower than the defined pivot
    low_index = left_index - 1
    for i in range(left_index, right_index):
        if arr[i] <= pivot:
            low_index += 1
            swap(arr, i, low_index)

    #  place the value of the pivot location in the middle.
    # all numbers smaller than the pivot are on the left_index, larger on the right_index. 
    swap(arr, right_index, low_index + 1)
    # return the pivot index point
    return low_index + 1

def swap(arr, i, low_index):
    temp = arr[i]
    arr[i] = arr[low_index]
    arr[low_index] = temp