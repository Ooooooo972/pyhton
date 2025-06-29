def divisible5(n):
  if(n%5==0):
    return True
  return False

a=[1,5,65,54,85,65,78,54,55]



f= list(filter(divisible5,a))
print(f)