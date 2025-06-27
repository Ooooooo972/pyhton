class Empolyee:
  a=1
class progurammer(Empolyee):
  b=2

class coder(progurammer):
  c=3


o=Empolyee()
print(o.a)
o=progurammer()
print(o.a,o.b)
o=coder()
print(o.a,o.b,o.c)  