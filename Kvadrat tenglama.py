import math
print('A teng emas 0 ga. Ax*x+Bx+C')
a=int(input('A='))
b=int(input('B='))
c=int(input('C='))
d=b*b-4*a*c
if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print('x1=',x1)
    print('x2=',x2)
elif d==0:
    x=-b/(2*a)
    print('x=',x)
else : 
    print('yechimga ega emas')
