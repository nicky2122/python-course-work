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
        