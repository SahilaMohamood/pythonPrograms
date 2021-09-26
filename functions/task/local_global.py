x=5
a=7

def loc():
   # x=5
   global x,a
   a+=2
   x+=10
   print("local is",x,a)
loc()
print("global is",x,a)