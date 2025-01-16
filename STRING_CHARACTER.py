def string_chars():
    string=input("Enter the string: ")
    no_of_lines=int(input("No of lines: "))

    if no_of_lines>len(string):
        print("------Not Possible To Display------")
        return
    else:
        no_of_chars_in_each_line=len(string)//no_of_lines
        for i in range(no_of_lines):
            print(string[i*no_of_chars_in_each_line : (i+1)*no_of_chars_in_each_line]) 
string_chars()         