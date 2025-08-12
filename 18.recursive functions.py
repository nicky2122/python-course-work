'''def recursive_function():
    if base_case_condition:
        return some_value
    else:
        return recursive_function()
'''
#recursive factorial function
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the value: "))
print(f"factorial of {n}",{factorial(n)})
print(factorial(n))#used this one also direct

    
# Recursive function to find sum of numbers from 1 to n
def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)  
n = int(input("Enter a number: "))
print(sum_of_numbers(n))

#Reverse a String
def reverse_string(s):
    if s=="":
        return s
    else:
        return reverse_string(s[1:])+s[0]
print(reverse_string("hello"))

#Find GCD (Greatest Common Divisor)
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(60,48)) 
   





