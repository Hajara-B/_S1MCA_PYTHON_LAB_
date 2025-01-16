class Publisher:
    def __init__(self,name):
        self.name=name
    def display__publisher(self):
        return f"Publisher: {self.name} "

class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display__book(self):
        return f"Title: {self.title} , Author:{self.author} "

class Python__Book(Book):
    def __init__(self,name,title,author,price,pages):
        super().__init__(name,title,author)
        self.price=price
        self.pages=pages
    def display__Python__Book(self):
        return f"{self.display__publisher()} , {self.display__book()} , Price: ${self.price} , Pages:{self.pages}"

name=input("Publisher: ")
title=input("Title: ")
author=input("Author: ") 
price=int(input("Price: ")) 
pages=int(input("Pages: "))

book=Python__Book(name,title,author,price,pages)

print(book.display__Python__Book())
           
