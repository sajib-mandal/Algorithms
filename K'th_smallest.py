# 1st solution

import random
def randomized_select(arr, p, r, i):
    if p == r:
        return arr[p]
    q = randomized_partition(arr, p, r)
    k = q - p + 1
    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr, p, q - 1, i)
    else:
        return randomized_select(arr, q + 1, r, i - k)

def randomized_partition(arr, p, r):
    j = random.randrange(p, r)
    (arr[r], arr[j]) = (arr[j], arr[r])
    return partition(arr, p, r)

def partition(arr, p, r):
    k = arr[r]
    j = p - 1
    for l in range(p, r):
        if arr[l] <= k:
            j += 1
            (arr[j], arr[l]) = (arr[l], arr[j])
    (arr[j + 1], arr[r]) = (arr[r], arr[j + 1])
    return j + 1

if __name__ == '__main__':
    arr = [12, 3, 5, 7, 4, 19, 26]
    i = 3
    print("K'th smallest element is", randomized_select(arr, 0, len(arr) - 1, i))

#........Answer is 5.........


# 2nd solution

import random
def randomized_select(arr, p, r, i):
    if p == r:
        return arr[p]
    q = randomized_partition(arr, p, r)
    k = q - p + 1
    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr, p, q - 1, i)
    else:
        return randomized_select(arr, q + 1, r, i - k)

def randomized_partition(arr, p, r):
    j = random.randrange(p, r)
    (arr[r], arr[j]) = (arr[j], arr[r])
    return partition(arr, p, r)

def partition(arr, p, r):
    k = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= k:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[r]) = (arr[r], arr[i + 1])
    return i + 1

if __name__ == '__main__':
    arr = [12, 3, 5, 7, 4, 19, 26]
    i = 3
    print("K'th smallest element is", randomized_select(arr, 0, len(arr) - 1, i))

#...............Answer is 5 ...............
