"""
Maximum sum Subarray of Size k:
Given an array of positive integers, and a positive number k,
find the maximum sum of any contiguous subarray of size k.

Explanation: Here the subarray [1, 7] is the sum of the maximum sum.

Ex- Input: [3, 5, 2, 1, 7], k=2, Output: 8
"""


def getMaxSum(arr, k):
    maxSum = 0
    windowSum = 0
    l = 0

    for r in range(len(arr)):
        windowSum += arr[r]
        while (r - l + 1) == k:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[l]
            l += 1
    return maxSum

print(getMaxSum([3, 5, 2, 1, 7], 2))
