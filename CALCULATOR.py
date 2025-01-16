a=int(input("Enter number a: "))
b=int(input("Enter number b: "))

while(True):

    print("------CALCULATOR------")
    print("1.Addition '+' ")
    print("2.Substraction '-' ")
    print("3.Multiplication '*' ")
    print("4.Division '/' ")
    print("5.Exit")
    
    choice=input(">>>>>>>>>>>> Enter Your Choice <<<<<<<<<<<<\n ")

    if choice=='1':
        Addition=a+b
        print(f"SUM of {a} and {b} is {Addition}")
    elif choice=='2':
        Substraction=a-b
        print(f"DIFFERENCE of {a} and {b} is {Substraction}")
    elif choice=='3':
        Multiplication=a*b
        print(f"PRODUCT of {a} and {b} is {Multiplication}")
    elif choice=='4':
        Division=a/b
        print(f"QUOTIENT of {a} and {b} is {Division}")
    elif choice=='5':
        exit   
    else:
        print("invalid choice!!......")  
        break             

