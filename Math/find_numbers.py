# 1295. Find Numbers with Even Number of Digits

def find_numbers(nums):
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
    return count

print(find_numbers([12, 345, 2, 6, 7896])) # 2
print(find_numbers([555, 901, 482, 1771])) # 1

# MATH
def find_numbersM(nums):
    result = 0
    for num in nums:
        count = 0
        while num > 0:
            count += 1
            num = num // 10
        if count % 2 == 0:
            result += 1
    return result

print(find_numbersM([12, 345, 2, 6, 7896])) # 2
print(find_numbersM([555, 901, 482, 1721, 1000])) # 1


# Optimized version
def find_numbersM(nums):
    result = 0
    for num in nums:
        count = 0
        while num:
            count += 1
            num >>= 1
        if not count & 1:
            result += 1
    return 
