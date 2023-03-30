# Arrays Algorithms
## Kadane's algorithm
Kadane's algorithm is a dynamic programming algorithm used for finding the maximum subarray sum in an array of integers. It can be used in various applications where you need to find the maximum sum of a contiguous subarray within an array
```python
def max_subarray(nums):
    n = len(nums)
    max_sum = float('-inf')
    current_sum = 0
    for i in range(n):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6
print(max_subarray([5, 4, -1, 7, 8])) # 23

def maxSubArray(nums):
    maxSum = float('-inf')
    currentSum = 0
    for n in nums:
        currentSum = max(n, currentSum + n)
        if currentSum > maxSum:
            maxSum = currentSum
    return maxSum
   
```
