def linear_search(arr, target):
    """
    Searches for a given element 'x' in a list 'arr' using linear search algorithm.
    Returns the index of the element if found, else returns -1.
    """

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([18, 12, 9, 14, 77, 50, -1], 14)) # 3
print(linear_search([], 34)) # -1




def linear_search_recursive(arr, target, index):
    """
    Searches for a given element 'x' in a list 'arr' using recursive linear search algorithm.
    Returns the index of the element if found, else returns -1.
    """

    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index + 1)

print(linear_search_recursive([18, 12, 9, 14, 77, 50], 14, 0)) # 3
print(linear_search_recursive([], 34, 0)) # -1
