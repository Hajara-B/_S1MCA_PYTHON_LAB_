import math
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))

d=b**2-4*a*c

r1=(-b+math.sqrt(d))/(2*a)
r2=(-b-math.sqrt(d))/(2*a)
r=(-b*a)/2

if d>0:
    print(f"The Roots Are {r1} & {r2}")
elif(d==0):
     print(f" Root Is {r}")
else:
     print("The Roots Are Imaginary")     

