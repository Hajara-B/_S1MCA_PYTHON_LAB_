def len_of_longest():
    words=input("Enter the words: ").split()

    len_of_long=0
    for word in words:
        if len(word)>len_of_long:
            len_of_long=len(word)
    return len_of_long    
print(len_of_longest())        
    