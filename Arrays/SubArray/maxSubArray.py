# def subArray(arr):
    # O(n^3)
    # n = len(arr)
    # maximun = float('-inf')
    # for i in range(n):
    #     for j in range(i, n):
    #         currentSum = sum(arr[i:j+1])
    #         if currentSum > maximun:
    #             maximun = currentSum
    # return maximun
    
    # O(n^3)
    # maximun = float('-inf')
    # n = len(arr)
    # for i in range(n):
    #     for j in range(i, n):
    #         total = 0
    #         for k in range(i, j + 1):
    #             total += arr[k]
    #         if total > maximun:
    #             maximun = total
    # return maximun

    # Sliding window
    # maxSub = arr[0]
    # curSum = 0
    # for n in arr:
    #     if curSum < 0:
    #         curSum = 0
    #     curSum += n
    #     maxSub = max(maxSub, curSum)
    # return maxSub

    # Kadane's algorithm
def maxSubArray(nums):
    maxSum = float('-inf')
    currentSum = 0
    for n in nums:
        currentSum = max(n, currentSum + n)
        if currentSum > maxSum:
            maxSum = currentSum
    return maxSum
     
# # GPT
# def max_subarray(nums):
#     n = len(nums)
#     max_sum = float('-inf')
#     current_sum = 0
#     for i in range(n):
#         current_sum = max(nums[i], current_sum + nums[i])
#         max_sum = max(max_sum, current_sum)
#     return max_sum

# def max_subarray(nums):
#     n = len(nums)
#     max_sum = float('-inf')
#     current_sum = 0
#     for i in range(n):
#         current_sum = max(nums[i], current_sum + nums[i])
#         max_sum = max(max_sum, current_sum)
#     return max_sum


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6
print(max_subarray([5, 4, -1, 7, 8])) # 23
