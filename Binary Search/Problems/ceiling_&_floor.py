"""
we are simply using binary search algorithm here to search the ceiling index , 
because there only we will insert the incoming value .
ceiling value : its either equal to the target element , or the smallest value 
among the elements which r larger than target .
Example :
array = { 1 , 2 , 3 ,4 , 5 , 8 ,9 }
target = 5 , ceiling value = 5
target = 6 , ceiling value = 8
so if 6 is coming , it will take index of 8 only ,
Hope I was able to make you unserstand :)
"""



# return the index: smallest no >= target
def ceiling(arr, target):
    start = 0
    end = len(arr) - 1

    # but what if the target is greater than the greatest number in the array
    if target > arr[end]:
        return -1
    
    while start <= end:
        mid = start + (end - start) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return start

print(ceiling([2, 3, 5, 9, 14, 16, 18], 17)) # 6
print(ceiling([2, 3, 5, 9, 14, 16, 18], 100)) # -1


# return the index: greatest no <= target
def floor(arr, target):
    start = 0
    end = len(arr) - 1

    # Here no need above condition it's automatically give -1

    while start <= end:
        mid = start + (end - start) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(floor([2, 3, 5, 9, 14, 16, 18], 17)) # 5
print(floor([2, 3, 5, 9, 14, 16, 18], 1)) # -1 
