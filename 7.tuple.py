#tuples

#Accessing Tuple Elements
my_tuples=(22,21,33,45)
print(my_tuples[3])#indexing(45)
print(my_tuples[-2])#negative indexing(33)
print(my_tuples[0:])#slicing(22, 21, 33, 45)


#Operations on Tuples
tuple1=(1,2,3)
tuple2=(5,6,7)
a,b,c=tuple1
result=tuple2 + tuple2
print(result)#(5, 6, 7, 5, 6, 7)
print(tuple1 * 5)#(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
print(3 in tuple1)#True
print(6 not in tuple2)#False


#Tuple Methods
tuple=1,2,3,3,4,2,5
print(tuple.count(3))#2
print(tuple.index(3))#2


#Built-in Functions for Tuples
tuple=44,5,6,2,7
len(tuple)#5
max(44,5,6,2,7)#2
min(44,5,6,2,7)#44
sum(tuple)#64
