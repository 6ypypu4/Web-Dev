def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
  return len(nums) > 0 and nums[0] == nums[-1]

def make_pi():
  return [3, 1, 4]

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
  sum = 0
  for num in nums:
    sum += num
  return sum
  
def rotate_left3(nums):
  return nums[1:] + [nums[0]]

def reverse3(nums):
    return [nums[2], nums[1], nums[0]]

def max_end3(nums):
    max_val = max(nums[0], nums[-1])
    return [max_val, max_val, max_val]

def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) < 2:
        return sum(nums)
    return nums[0] + nums[1]

def middle_way(a, b):
  return [a[1]] + [b[1]]

def make_ends(a):
  return [a[0]] + [a[-1]]

def has23(nums):
  return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3


