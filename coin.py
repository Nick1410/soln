n=int(input())
x=int((n-4)/5)
y=n-5*x
z=0
if y%2==0:
    z=2
else:
    z=1
a=n-5*x-z
b=int(a/2)
c=x+z+b
print(c)
print(x)
print(z)
print(b)
