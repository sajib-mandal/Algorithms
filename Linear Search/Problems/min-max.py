# Min
def find_min(arr):
    min_val = float("inf")
    for val in arr:
        if val < min_val:
            min_val = val
    return min_val


print(find_min([18, 12, -7, -1, 3, 14, 28, -100])) # -100

def find_min1(arr):
    min_val = arr[0]
    for val in arr:
        if val < min_val:
            min_val = val
    return min_val


print(find_min1([18, 12, -7, -1, 3, 14, 28, -100])) # -100




# Max
def find_min(arr):
    max_val = float("-inf")
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val

print(find_min([18, 12, -7, -1, 3, 14, 28, -100, 200])) # 200




def find_min(arr):
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val

print(find_min([18, 12, -7, -1, 3, 14, 28, -100, 200])) # 200
