#1.even or odd
evenorodd=lambda i:"even" if i%2==0 else "odd"
print(evenorodd(4))
print(evenorodd(11))
#2.max of 2numbers
maxof2numbers=lambda a,b:a if a>b else b
print(maxof2numbers(4,23))
print(maxof2numbers(100,200))
#3.sorted elements
l=[(1,22),(22,2),(6,54)]
print(sorted(l,key=lambda i:i[1]))
print(sorted(l,key=lambda i:i[0]))
#dictionary in lambda
marks={"python" : 40, "java" : 35, "mysql" : 45}
l=sorted(marks.items(),key=lambda i:i[1])
print(l)
n=dict(sorted(marks.items(),key=lambda i:i[1]))
print(n)
m=dict(sorted(marks.items(),key=lambda i:i[1],reverse=True))
print(m)
#length on string
length = lambda s:len (s)
print(length("python programming"))
print(length("hello world"))
#4.filter method in even or odd
l=[1,2,3,4,5,6,7,11,10]
even=list(filter(lambda i:i%2==0,l))
odd=list(filter(lambda i:i%2!=0,l))
print(even)
print(odd)
#different 
l=["a","lamp","camp","sun","b","the"]
update=list(filter(lambda i:len(i)>=3,l))
print(update)
update=list(filter(lambda i:len(i)<=3,l))
print(update)
#5.map method square numbers
l=[1,2,3,4,5]
square=list(map(lambda i:i*i,l))
print(square)
#5.map method multiple numbers
l=[1,2,3,4,5]
multiple=list(map(lambda i:i*3,l))
print(multiple)
#6.vowels in lambda
l="python"
vowels='aeiouAEIOU'
n=list(map(lambda i:'*'if i in vowels else i,l ))
print(n)
#upper cases in lambda
names="nicky","anjali","moksha","arvindh"
n=list(map(lambda i:i.upper(),names))
print(n)
#title cases in lambda
names="nicky","anjali","moksha","arvindh"
n=list(map(lambda i:i.title(),names))
print(n)
#update
l=[1,2,3,4,5,6]
update=list(map(lambda i: i+10,l))
print(update)
l=[11,12,13,14,15,16]
update=list(map(lambda i: i-10,l))
print(update)
l=[1,2,3,4,5]
l=list(map(lambda i:i,enumerate(l)))
print(l)




