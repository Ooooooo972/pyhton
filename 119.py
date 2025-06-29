from functools import reduce
l=[555,77,254,4,63,45,587]


def greater(a,b):
  if(a>b):
    return a
  return b


print(reduce(greater,l))