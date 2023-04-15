def search_2D_array(arr, target):
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == target:
                return [r, c]
    return [-1, -1]

print(search_2D_array([[23, 4, 1], [18, 12, 3, 9], [78, 99, 34, 56], [18, 12]], 34)) # [2, 2] index
print(search_2D_array([[23, 4, 1], [18, 12, 3, 9], [78, 99, 34, 56], [18, 12]], 100)) # [-1, -1]


# MAX value in 2D array
def search_2D_array_max(arr):
    max_val = arr[0][0]
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] > max_val:
                max_val = arr[r][c]
    return max_val

print(search_2D_array_max([[23, 4, 1], [18, 12, 3, 9], [78, 99, 34, 56], [18, 12]])) # 99
print(search_2D_array_max([[23, 4, 1], [18, 12, 3, 9], [78, 99, 34, 56], [18, 12, 150]])) # 150



# MIN value in 2D array
def search_2D_array_min(arr):
    max_val = arr[0][0]
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] < max_val:
                max_val = arr[r][c]
    return max_val

print(search_2D_array_min([[23, 4, 1], [18, 12, 3, 9], [78, 99, 34, 56], [18, 12]])) # 1
print(search_2D_array_min([[23, 4, 1], [18, 12, 3, 9], [78, 99, 34, 56], [18, 12, -10]])) # -10
