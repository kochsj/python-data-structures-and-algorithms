def quick_sort(arr, left_index, right_index):
    # base case - the array has less than 2 elements
    if right_index - left_index <= 0:
        return
    # get the pivot position
    pivot_position = partition(arr, left_index, right_index)

    #recursively sort the sub array to the left of the pivot
    quick_sort(arr, left_index, pivot_position-1)

    #recursively sort the sub array to the right of the pivot
    quick_sort(arr, pivot_position+1, right_index)

def partition(arr, left_index, right_index):

    pivot = right_index
    pivot_value = arr[pivot]
    right_index -= 1

    while True:
        #[0,5,2,6,8] pivot value = 4
        while arr[left_index] < pivot_value:
            left_index += 1 #index 1
        while arr[right_index] > pivot_value:
            right_index -= 1
        if left_index >= right_index:
            break
        else:
            swap(arr, left_index, right_index)

    arr[left_index], arr[pivot] = arr[pivot], arr[left_index]

    return left_index

def swap(arr, left_index, right_index):
    arr[left_index], arr[right_index] = arr[right_index], arr[left_index]