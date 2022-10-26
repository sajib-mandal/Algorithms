"""
209. Minimum Size Subarray Sum
Ex- target = 7, nums = [2,3,1,2,4,3], output: 2
    target = 4, nums = [1,4,4], output: 1
    target = 11, nums = [1,1,1,1,1,1,1,1], output: 0
"""


def minSize(nums, target):
    if not nums:
        return 0
    l, total = 0, 0
    res = float("inf")
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(res, r - l + 1)
            total -= nums[l]
            l += 1

    return 0 if res == float("inf") else res


print(minSize([3, 5, 2, 1, 7], 2))
