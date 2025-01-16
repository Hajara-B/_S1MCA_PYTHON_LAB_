class BankAccount:
    def __init__(self,ac_no,name,ac_ty,balance=0):
        self.ac_no=ac_no
        self.name=name
        self.ac_ty=ac_ty
        self.balance=balance

    def deposit(self,amount):
        if amount<=0:
            print("invalid amount")
        else:
            self.balance+=amount
            print(f"balance is: {self.balance}")

    def withdraw(self,amount):
        if amount<=0:
            print("invalid amount")
        elif amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(f"balance is: {self.balance}")

    def display(self):
         print("---Account Details---")
         print(f"Account Number: {self.ac_no}")
         print(f"Account Holder's Name: {self.name}")
         print(f"Account Type: {self.ac_ty}")
         print(f"Account Balance: {self.balance}")

ac_no=float(input("Account Number: "))   
name=input("Account Holder's Name: ")
ac_ty=input("Account Type: ")
balance=float(input("Account Balance: "))

account=BankAccount(ac_no,name,ac_ty,balance)



while True:
    print("\n---Menu---\n 1.DEPOSIT MONEY\n 2.WITHDRAW MONEY\n 3.DISPLAY\n 4.EXIT\n")

    choice=input("Enter your choice: ")
    
    if choice=='1':
        amount=float(input("Enter the amount to deposit: "))
        account.deposit(amount)             
    elif choice=='2':
        amount=float(input("Enter the amount to withdraw: "))
        account.withdraw(amount) 
    elif choice=='3':
        account.display()
    elif choice=='4':
        print("Exit")
        break
    else:
        print("Invalid choice")
        
        
        

        

        
              
              


              

            
    

            


              
              


              

            

        
              
              


              

            
