class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width

    def area(self):
        return self.__length*self.__width

    def __lt__(self,other):
        return self.area() < other.area()

    def compare__area(self,other):
        if self.area() > other.area():
            return "rectangle1 has the larger area"
        elif self.area() < other.area():
            return "rectangle2 has the larger area"
        else:
            return "both rectangles has the same area"
        
print("---RECTANGLE1---")
length1=float(input("length1: "))
width1=float(input("width1: "))

rectangle1=Rectangle(length1,width1)

print("---RECTANGLE1---")
length2=float(input("length2: "))
width2=float(input("width2: "))

rectangle2=Rectangle(length2,width2)

print(rectangle1.compare__area(rectangle2))
