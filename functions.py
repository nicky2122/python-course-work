#1.add two numbers
def add(a,b):
    return a+b
print(add(5,10))
#2.square a number
def square(num):
    return num*6
number=int(input("enter the number: "))
result=square(number)
print("square of",number,"is",result)    
 #Area of a Circle
import math  
def area_of_circle(radius):
    return math.pi * radius ** 2
r = float(input("Enter the radius of the circle: "))
print("Area of the circle is:", area_of_circle(r))
