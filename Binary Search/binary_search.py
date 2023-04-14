# Recursive

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    def search(arr, target, start, end):
        if start > end:
            return -1
        
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return search(arr, target, start, mid - 1)
        else:
            return search(arr, target, mid + 1, end)
    return search(arr, target, start, end)



print(binary_search([1, 2, 3, 4, 5], 1)) # 0
print(binary_search([1, 2, 3, 4, 5], 2)) # 1
print(binary_search([1, 2, 3, 4, 5], 3)) # 2
print(binary_search([1, 2, 3, 4, 5], 4)) # 3
print(binary_search([1, 2, 3, 4, 5], 5)) # 4
print(binary_search([1, 2, 3, 4, 5], 6)) # -1
