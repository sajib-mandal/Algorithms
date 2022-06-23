def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])


arr = [4, 7, 1, 9, 5, 8]
bubbleSort(arr)
print(arr)
