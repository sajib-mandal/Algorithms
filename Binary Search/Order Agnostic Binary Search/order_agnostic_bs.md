# Order Agnostic Binary Search
Order-agnostic binary search is a search algorithm that can find the position of a target element in a given list, regardless of whether the list is sorted in ascending or descending order. Here's a Python implementation of order-agnostic binary search:
```python
def order_agnostic_binary_search(arr, target):
    left, right = 0, len(arr) - 1
    is_ascending = arr[left] < arr[right]

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if is_ascending:
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[mid] > target:
                left = mid + 1
            else:
                right = mid - 1

    return -1


print(order_agnostic_binary_search([-18, -12, -4, 0, 2, 3, 4, 15, 16, 18, 22, 45, 89], 22)) # 10
print(order_agnostic_binary_search([99, 80, 75, 22, 11, 10, 5, 2, -3], 22)) # 3
```
The `order_agnostic_binary_search` function takes in two arguments: `arr`, the list to search, and `target`, the element to search for. It starts by initializing the left and right bounds of the search to the first and last indices of the list, respectively. It then determines whether the list is sorted in ascending or descending order by comparing the first and last elements of the list.
The function then enters a loop that runs until the left bound is greater than the right bound. Within the loop, it calculates the midpoint of the search range and checks whether the value at that position is equal to the target. If it is, the function returns the index of that position.
If the midpoint value is less than the target and the list is sorted in ascending order, the left bound is updated to `mid + 1` to discard the left half of the search range. Otherwise, if the midpoint value is greater than the target and the list is sorted in descending order, the left bound is also updated to `mid + 1`. Otherwise, if the midpoint value is greater than the target and the list is sorted in ascending order, the right bound is updated to `mid - 1` to discard the right half of the search range. Otherwise, if the midpoint value is less than the target and the list is sorted in descending order, the right bound is also updated to `mid - 1`.
If the target is not found in the list, the function returns -1.
