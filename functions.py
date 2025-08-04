'''# #function program
def add(a,b):
     return a+b
a,b=map(int,input("enter the number: ").split())
print(f"{add(a,b)}")


def mul(n,m):
     return n*m
n,m=map(int,input("enter the number: ").split())
print(f"{mul(n,m)}")


def even(num):
#     if num % 2 ==0:
#         return True
#     else:
#         return False
# num = int(input("enter the number")) 
# if even(num):
#     print(num,"is a even numbe: ")
# else:
     print(num,"is not a even number: ")   
       

# #type of function
# #1.bulit function
def square(num):
    l=[]
    for i in num:
        num=l.append(i**2)
    return l    
num=list(map(int,input(" ").split(' ')))        
print("sqaure of num:",square(num))
# #type of function
# #1.bulit function

def message(name,age=23):
    return f"hello",{name}
print(f"hello{message(guiu,age)}")

def even_count(num):
     count=0
     for i in num:
          if num%2==0:
               count+=1
               return count
num=int(input())
print(even_count(num))         

def greet(name, age):
 print(f"{name}, {age}")
greet("Alice", 25)'''
def add(*a):
 return sum(a)
print(add(1, 2, 3, 4, 5))