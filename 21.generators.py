def feed(l):
    for i in l:
        yield i
l=['1...100','101...200','201...301']
load=feed(l)
print(next(load)) 
print(next(load)) 
print(next(load))

# 1: Generator to Yield Squares of Numbers
def square(n):
    for i in range(n):
        yield i*i
for i in square(5):
    print(i)   

#2: Generator to Yield Vowels from a String        
def string(s):
    vol='aeiouAEIOU'
    for i in s:
       if i in vol:
           yield i
for i in string('nicky'):
    print(i)  


#3: Generator for Multiplication Table
def multiple(n):
    for i in range(1,11):
        yield n * i
for i in multiple(5):
    print(i) 

#4: Generator Expression for Cube of Numbers
'''def cube(n):
    for i in range(1,5):
        yield n**3
for s in cube(4):
    print(s)
    '''
cube=(x**3 for x in range(1,6))
for i in cube:
    print(i) 

square=(x**2 for x in range(1,6))
for i in square:
    print(i) 

'''def cube(n):
    for i in range(n):
        yield n**i 
for i in cube(5):
    print(i)            
   '''

#5: Generator to Filter Odd Numbers in a List
def odd_num(n):
    for i in n:
        if i%2!=0:
            yield i
l=[1,2,3,4,5,11,12]
for s in odd_num(l):
    print(s) 

def even_num(n):
    for i in n:
        if i%2==0:
            yield i
l=[1,2,3,4,5,11,12]
for s in even_num(l):
    print(s)                
                     

#6: Generator to Count Down From N to 1
def count(n):
    while n>0:
        yield n
        n-=1
for i in count(5):
    print(i)

'''def count(n):
    count=0
    for i in range(n):
        yield i
        count-=1
for s in count(6):
    print(s)       
'''
def countdown(n):
    for i in range(n, 0, -1):  # start at n, go down to 1
        yield i
