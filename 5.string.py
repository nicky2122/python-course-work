name='nicky'
name2="anjali"
name3='''hello world'''
print(name)#nicky
print(name2)#anjali
print(name3)#hello world

#operation  on strings
#concatention
str1='computer'
str2='python'
result=str1+''+str2
print(result) #computerpython

#repetition
print('nicky!'* 5)
#nicky!nicky!nicky!nicky!nicky!

#indexing
text='nikhitha'
print(text[1])#i
print(text[-1])#a
print(text[0])#n
print(text[5])#t

#slicing
text='nikhitha'
print(text[0:4])#nikh
print(text[0:])#nikhitha
print(text[-3:])#tha

#membership
text='nikhitha'
print('nikhitha'in text)#True
print('anjali'not in text)#True


#built in string
#len
text='nikhitha'
print(len(text))#8

#max()andmin()
text='nikhitha'
print(max('nikhitha'))#t
print(min('nikhitha'))#a

#sorted()
text='nikhitha'
print(sorted("nikhitha"))#['a', 'h', 'h', 'i', 'i', 'k', 'n', 't']


#chr() and odr()
print(ord('D')) #68
print(chr(100))#d



#case conversion method
print("hello".upper())#HELLO
print("HELLO".lower())#hello
print("nicky".capitalize())#Nicky
print("nicky anjali".title())#Nicky Anjali
print("nIckY".swapcase())#NiCKy
print("ß".casefold())#ss


#Alignment & Formatting Methods
print("nicky".center(20, "*"))#*******nicky********
print("nicky".ljust(16, "&"))#nicky&&&&&&&&&&&
print("nicky".rjust(15, "&"))#&&&&&&&&&&nicky
print("678".zfill(8))#00000678
print("name:{}, age:{}".format("nicky",22))#name:nicky, age:22
print("{name} is {age}".format_map({'name':'nicky','age':22}))#nicky is 22



#Search & Find Methods
print("nikhitha".find("h"))#3
print("nikhitha".rfind("k"))#2
print("nikhitha".index("k"))#2
print("nikhitha".rindex("i"))#4
print("nikhitha".count("i"))#2

#String Testing Methods (Boolean)
print("moksha".startswith("mo"))#True
print("moksha".endswith("sha"))#True
print("Moksha".isalpha())#True
print("abc223".isalnum())#True
print("nikhitha".islower())#True
print("nikhitha".isupper())#False
print(" ".isspace())#True
print("Nikhitha Anjali".istitle())#True
print("nikhitha3".isidentifier())#True

#Replace & Modify Methods
print("nikhitha".replace("i","l"))#nlkhltha
print("nikhitha".translate(str.maketrans("n","l")))#likhitha
print("nikhitha".maketrans("tha","&%4"))#{116: 38, 104: 37, 97: 52}


#Splitting & Joining Methods
print("n,i,c,k,y".split(","))#['n', 'i', 'c', 'k', 'y']
print("n,i,c,k,y".rsplit(",",3))#['n,i', 'c', 'k', 'y']
print("nikhitha\nanjali".splitlines())#['nikhitha', 'anjali']
print(" ".join(["nicky", "anjali"]))#nicky anjali
print("apple-pie".partition("-"))#('apple', '-', 'pie')
print("apple-pie".rpartition("-"))#('apple', '-', 'pie')


#Whitespace & Trimming Methods
print("Nicky".strip())#Nicky
print("----nicky".lstrip("-"))#nicky
print("nicky-----".rstrip("-"))#nicky

#Encoding & Decoding Methods
print("nicky".encode("utf-8"))#b'nicky'
print(b"nicky".decode("utf-8"))#nicky


