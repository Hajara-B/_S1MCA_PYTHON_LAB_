class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

    def compare_area(self,other):
        if self.area() > other.area():
            return "rectangle1 has the larger area"
        elif self.area() < other.area():
            return "rectangle2 has the larger area"
        else:
            return "both rectangles have the same area"

print("---RECTANGLE 1---")
length1=float(input("length1: "))
breadth1=float(input("breadth1: "))

rectangle1=Rectangle(length1,breadth1)
     
print("---RECTANGLE 2---")
length2=float(input("length2: "))
breadth2=float(input("breadth2: "))

rectangle2=Rectangle(length2,breadth2)

print(rectangle1.compare_area(rectangle2))
     


        
     

        
