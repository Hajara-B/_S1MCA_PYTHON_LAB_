a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
c=int(input("Enter number c: "))
if a>b and a>c:
    print(f"{a} is the largest")
if b>c and b>a:
    print(f"{b} is the largest")  
else:
    print(f"{c} is the largest")      