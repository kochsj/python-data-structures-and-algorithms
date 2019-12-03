def insert_shift_array(lst, num):
    middle = (len(lst)+ 1) // 2
    new_list = []
    for i in range(middle):
        new_list.append(lst[i])
    new_list.append(num)
    for i in range(middle, len(lst)):
        new_list.append(lst[i])
    return(new_list)        


##################################### 
# Other Approach
# def insert_shift_array(lst, num):
#   new_lst = []
#   middle = (len(lst) + 1) // 2
#   for i in range(len(lst) + 1):
#     if i < middle:
#       new_lst.append(lst[i])
#     elif i == middle:
#       new_lst.append(num)
#     elif i > middle:
#       new_lst.append(lst[i - 1])
#   print(new_lst)
# insert_shift_array([2,4,6,8], 5)

def remove_middle(lst):
  middle = (len(lst)) // 2
  return(lst[:middle:1]+lst[middle+1::1])
