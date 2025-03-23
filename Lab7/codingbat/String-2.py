def double_char(str):
    new_str = ""
    for char in str:
        new_str += char*2
    return new_str

def count_hi(str):
  sum = 0
  for i in range (0, len(str) - 1):
     if(str[i] == 'h' and str[i+1] == 'i'):
        sum +=1
  return sum

def cat_dog(str):
  dog, cat = 0, 0
  for i in range (0, len(str) - 2):
     if(str[i] == 'd' and str[i+1] == 'o' and str[i+2] == 'g'):
        dog +=1
     elif(str[i] == 'c' and str[i+1] == 'a' and str[i+2] == 't'):
        cat +=1
  return cat == dog

def count_code(str):
   sum = 0
   for i in range(0, len(str) - 3):
      if(str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e'):
         sum += 1
   return sum

def end_other(a, b):
    a_lower = a.lower()
    b_lower = b.lower()
    return a_lower.endswith(b_lower) or b_lower.endswith(a_lower)

def xyz_there(str):
    for i in range(len(str) - 2):
        if str[i:i+3] == 'xyz':
            if i == 0 or str[i-1] != '.':
                return True
    return False
