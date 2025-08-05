#for var in sequence(list/tuple/set/dic/str/(range(start,stop)))
list=[1,2,3]
for i in list:
    print(i)
tuple=(1,2,3)
for i in tuple:
    print(i)
set={1,2,3}
for i in set:
    print(i) 
dic={'key1':'val1','key2':'val2'}
for i in dic:
     print(i)
dic={'key1':'val1','key2':'val2'}
for i in dic:
     print(i,dic[i])
dic={'key1':'val1','key2':'val2'}
for i in dic.keys():
     print(i,dic[i])
dic={'key1':'val1','key2':'val2'}
for i in dic.values():
     print(i)               
dic={'key1':'val1','key2':'val2'}
for ind, i in enumerate(dic):
     print(ind,i,dic[i])
str="python"
for i in str:
     print(i)
str="python"
for i in str:
     print(i)


for i in range(1,6):
     print(i)
for i in range(2,10):
     print(i)
for i in range(2,10,2):
     print(i)
for i in range(5,2,3):
     print(i)
for i in range(12,4,-3):
     print(i)
for i in range(16,2,-7):
     print(i)
l="python"
n=len(l)
for i in range(n):
     print(i)
l="python"
n=len(l)
for i in range(n):
     print(i,l[i])          
l="python"
n=len(l)
for i in range(len(l)):
     print(i,l[i])
t=(1,2,3)
n=len(t)
for i in range(n):
     print(i,t[i])
t=(1,2,3)
n=len(t)
for i in range(len(t)):
     print(i,t[i])     
d={'key1':'val1','key2':'val2','key3':'val3'}
n=len(d)
for i in range(n):
     print(i)
d={'key1':'val1','key2':'val2','key3':'val3'}
n=len(d)
for i in range(len(d)):
     print(i)
d={'key1':'val1','key2':'val2','key3':'val3'}
n=len(d)
for ind,i in enumerate(d):
     print(ind,i,d[i])


'''Inti
while con:
  upda'''
i=1
while i<=10:
     print(i)
     i+=2                
i=10
while i>=1:
     print(i)
     i-=1 
i=2
while i<=22:
     print(i)
     i+=5 
l=[1,2,3,444,11,21,1,2,3,32,22,1,2 ]
while 1 in l:
     l.remove(1)
     print(l)
l=[1,2,3,444,11,21,1,2,3,32,22,1,2 ]
while l:
     l.pop(0)
     print(l)
l=[1,2,3,444,11,21,1,2,3,32,22,1,2 ]
ind=0
n=len(l)
while ind<n:
     print(l[ind])
     ind+=1
t=('input','output','type','if','else')
ind=0
n=len(t)
while ind<n:
  print(t[ind])
  ind+=1
s='Control Statements'
ind=0
n=len(s)
while ind<n:
  print(s[ind])
  ind+=1
'''d={'key1':'val1','key2':'val2','key3':'val3'}
k=tuple(d.keys())
i=0
while i<len(k):
  print(k[i],d[k[i]])
  i+=1'''
#2. Sum of First 5 Natural Numbers
i=1
sum=0
while i<=5:
     sum+=i
     i+=1
print("sum is: ",sum)
#3. Reverse a Number
num = 1234
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10
print("Reversed:", rev)

             

