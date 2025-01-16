word=input("Enter a word: ")
letter=input("Enter the letter:")
count=0
for i in word:
    if letter==i:
        count+=1
print(f"The Count Of The Letter {letter} In The Word {word} Is {count}")        
