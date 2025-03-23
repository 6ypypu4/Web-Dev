def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

def big_diff(nums):
    min_val = nums[0]
    max_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return max_val - min_val

def centered_average(nums):
    min_val = min(nums)
    max_val = max(nums)
    total = sum(nums) - min_val - max_val
    return total // (len(nums) - 2)

def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 1  
        else:
            total += nums[i]
        i += 1
    return total

def sum67(nums):
    total = 0
    skip = False
    for num in nums:
        if num == 6:
            skip = True
        elif skip and num == 7:
            skip = False
        elif not skip:
            total += num
    return total

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False

