def greatest(a,b,c):
   if(a>b and a>c):
      return a
   elif(b>a and b>c):
      return b
   elif(c>a and c>b):
      return c
   


a=2
b=3
c=9
print(f"The greatest number is, {greatest(a,b,c)}")
   