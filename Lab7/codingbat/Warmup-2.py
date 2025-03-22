def string_times(str, n):
  copy = ""
  for i in range ( 1, n+1):
    copy += str
  return copy

def front_times(str, n):
  copy = ""
  if len(str) >= 3:
    str = str[:3]
  for i in range (0, n):
    copy += str
  return copy

def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

def string_splosion(str):
  result = ""
  for i in range(len(str)+1):
    result += str[:i]
  return result

def last2(str):
  if len(str) < 2:
    return 0
  
  last2 = str[len(str)-2:]
  count = 0
  
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count

def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count = count + 1

  return count

def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):  
    if nums[i] == 9:
      return True
  return False

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

def string_match(a, b):
    x = min(len(a), len(b))
    i = 0
    back = False
    amount = 0
    while(i < x):
        if(a[i] == b[i]):
            if back:
              amount +=1
            back = True
        else:
            back = False
        i += 1
    return amount
