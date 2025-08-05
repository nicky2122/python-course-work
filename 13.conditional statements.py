data={
    'anjali@gmail.com':'1234',
    'nikhitha@gmail.com':'2222',
    'arvind@gmail.com':'5555',
    'moksha@gmail.com':'7777',
    }
email,password=input("enter the email and password: ").split()
if data.get(email)== password:
    print('login successfull')
else:
    print('invalid login')

 #1. Check if a number is positive, negative or zero
num=int(input("enter the number: "))
if num>0:
    print("postive number")
elif num<0:
    print("negative number")
else:
    print("zero")

#2. Check if a number is even or odd
num=int(input("enter the number: "))
if num%2==0:
    print("even number")
else:
    print("odd number")

#3. Check if a character is a vowel or consonant
char=input("enter the vowels: ")
if char in "aeiou":
    print("vowels")
else:
    print("consonants")
  
 #4. Find the largest among three numbers
num=int(input("enter first numbers: "))
num2=int(input("enter second numbers: "))  
num3=int(input("enter third numbers: "))
if num>num2 and num>num3:
    print("largest number is:",num)
elif num2>num and num2>num3:
    print("largest number is:",num2)
else:
    print("largest number is:",num3)    

# 6. Check if a number is divisible by 5 and 11
num=int(input("enter the number:"))
if num%5==0 and num%11==0:
    print("Divisible by both 5 and 11")
else:
    print("not divisible by both")

#7. Check if a person is eligible to vote
age=int(input("enter the age:"))
if age>=18:
    print("is aligible to vote")
else:
    print("not eligible to vote")

#8. Simple grading system
marks=int(input("enter the grads:"))
if marks>=90:
    print("grade A+")
elif marks>=85:
    print("grade is A")
elif marks>=75:
    print("grade isB+")
elif marks>=65:
    print("grade is B")
elif marks>=50:
    print("grade is C")
else:
    print("fail")


