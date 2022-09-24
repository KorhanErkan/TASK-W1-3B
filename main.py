def is_prime(num):
  i = 3
  if (num<2):
    return False
  elif (num==2):
    return True
  elif (num%2==0):
    return False
  while i<int(num/2):
    if (num%i == 0):
      return False
    else:
      i+=2
  return True

print(is_prime(5))
