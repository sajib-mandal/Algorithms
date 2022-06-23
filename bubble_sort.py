# 1st version

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])


arr = [4, 7, 1, 9, 5, 8]
bubbleSort(arr)
print(arr)



# 2nd version

def bubbleSort(arr):
    n = len(arr)
    swap = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swap = True
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
        if not swap:
            return


arr = [9, 1, 6, 8, 2, 4, 5, 1]
bubbleSort(arr)
#print(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
