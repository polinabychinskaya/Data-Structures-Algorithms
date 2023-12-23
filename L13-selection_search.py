# Instead of swapping the cards as was done with the bubble sort, 
# we are going to scan through the cards and select the smallest value
# The algorithm maintains both the sorted and unsorted values within the same sequence
# structure
def selectionSort(elements):
    size = len(elements)
    for i in range(size - 1):
        # Assume the ith element is the smallest.
        smallest_value_index = i
        # Determine if any other element contains a smaller value.
        for j in range(i+1, size):
            if elements[j] < elements[smallest_value_index]:
                smallest_value_index = j
    # Swap the ith value and smallNdx value only if the smallest value is
    # not already in its proper position. Some implementations omit testing
    # the condition and always swap the two values.
        if smallest_value_index != i:
            tmp = elements[i]
            elements[i] = elements[smallest_value_index]
            elements[smallest_value_index] = tmp
    return elements

elements = [1, 5, 0, 35, 65, 3]
print(selectionSort(elements))

# Time complexity O(n^2)