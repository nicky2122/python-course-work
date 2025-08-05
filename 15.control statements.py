#break statements
for i in range(1,6):
    if i==5:
        break
    print(i)
for i in range(10,21):
    if i==15:
        break
    print(i)
for i in range(1,10):
    if i==23:
        break
    print(i)
i=1    
while i<5:
    if i==4:
        break
    print(i)
    i+=1
i=0
while i<10:
    if i==12:
        break
    print(i)
    i+=1
#continue statements
for i in range(1,10):
    if i%2==0:
        continue
    print(i)
for i in range(1,10):
    if i==6:
        continue
    print(i)
i=0
while i<5:
    i+=1
    if i==3:
        continue
    print(i)
i=1
while i<10:
    i+=2
    if i==6:
        continue
    print(i)                   
 # for loop with else
 # No break — else runs
for i in range(1,5):
    print(i)
else:
    print("for loop finishe without break")
#With break — else skipped
for i in range(1,6):
    if i==5:
        break
    print(i)
else:
    print("loop finished")
for i in range(1,6):
    if i==10:
        break
    print(i)
else:
    print("loop finished")
#2. while loop with else
#No break — else runs
i=1
while i<5:
    print(i)
    i+=1
else:
    print("while loop ended normal")
i=0
while i<10:
    if i==6:
        break
    print(i)
    i+=1
else:
    print("loop will enede without break") 
i=0
while i<10:
    if i==15:
        break
    print(i)
    i+=1
else:
    print("loop will enede without break")                      


