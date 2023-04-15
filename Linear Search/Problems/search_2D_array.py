def search_2D_array(arr, target):
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == target:
                return [r, c] # index
    return -1




print(search_2D_array([[23, 4, 1], [18, 12, 3, 9], [78, 99, 34, 56], [18, 12]], 34)) # [2, 2]
print(search_2D_array([[23, 4, 1], [18, 12, 3, 9], [78, 99, 34, 56], [18, 12]], 100)) # -1
