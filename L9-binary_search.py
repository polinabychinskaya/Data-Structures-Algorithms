def binary_search(value, value_list):

    left_limit = 0 
    right_limit = len(value_list) - 1
    mid_index = 0 

    while left_limit <= right_limit:
        mid_index = (left_limit + right_limit) // 2
        median = value_list[mid_index]
        if value == median:
            return mid_index
        if median < value:
            left_limit = mid_index + 1
        else:
            right_limit = mid_index - 1
    return 'Value DNE'

print(binary_search(67, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

def binary_search_recursion(value, value_list, left_limit, right_limit):
    if right_limit < left_limit:
        return 'Value DNE'
    mid_index = (left_limit + right_limit) // 2
    median = value_list[mid_index]
    if median == value:
        return mid_index
    if median < value:
        left_limit = mid_index + 1
    else:
        right_limit = mid_index - 1
    return binary_search_recursion(value, value_list, left_limit, right_limit)

value_list = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search_recursion(2, value_list, 0, len(value_list)-1))