def linear_search_range(arr, target):
    for i in range(1, 4):
        if arr[i] == target:
            return True
    return False


print(linear_search_range([18, 12, -7, 3, 14, 28], 3)) # True



def linear_search_range1(arr, target, start, end):
    for i in range(start, end):
        if arr[i] == target:
            return i
    return -1



print(linear_search_range1([18, 12, -7, 3, 14, 28], 3, 1, 4)) # 3
print(linear_search_range1([18, 12, -7, 3, 14, 28], 14, 1, 4)) # -1
