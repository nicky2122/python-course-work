for row in range(5):
    for col in range(5):
        print("*",end=' ')
    print()
for row in range(5):
    for col in range(5):
        print(row,end=' ') 
    print()
for row in range(5):
    for col in range(5):
        print(col,end=' ') 
    print()
for row in range(5):
    for col in range(row+1):
        print("*",end=' ') 
    print()
for row in range(5):
    for col in range(5-row):
        print("*",end=' ')
    print()
for row in range(5):
    for col in range(5-row-1):
        print(" ",end=' ')
    for col1 in range(row+1):
        print("*",end=' ')    
    print()
for row in range(5):
    for col in range(row):
        print(" ",end=' ')
    for col1 in range(5-row):
        print("*",end=' ')    
    print() 
n=int(input("enet the number: "))
for row in rang(n):
    for col in range(n):
        if row==0 or col==0 or row-1==0 or col-1==0
        print("*",end=' ')
    else:
        print()                       
        