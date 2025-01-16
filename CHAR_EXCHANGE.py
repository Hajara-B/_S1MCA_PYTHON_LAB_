s=input("Enter a string: ")
if len(s)<2:
    print("Invalid!!")
else:
    new_string=s[-1]+s[1:-1]+s[0]
    print(f"New String Is --> {new_string}")
