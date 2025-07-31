#set creation syntax
my_set = {1,2,3,4}
empty_set = set()
set_with_duplicates = {1,2,4,5}
print(set_with_duplicates)

#3.operation on set
#a.membership testing
my_set = {1,2,3,4}
print(3 in my_set)
print(5 not in my_set)
#b.union methods |
set1={1,2,3}
set2={4,5,6}
result=set1 | set2
print(result)
#c.intersection &
set1={5,6,7}
set2={6,1,2}
result=set1 & set2
print(result)
#d.difference -
set1={1,2,3}
set2={3,4,5}
result=set1 - set2
print(result)
#e.symmetric difference ^
set1={1,2,3}
set2={2,3,4}
result=set1 ^ set2
print(result)
#f.subset <=
set1={1,2,3}
set2={3,4,5}
result=set1 <= set2
print(result)
#g.superset >=
set1={1,2,3}
set2={3,1}
result=set1 >= set2
print(result)
#h.disjoint sets()
set1={1,2,3}
set2={4,5,6}
result=(set1.isdisjoint(set2))
print(result)

#4.Built-in Methods for Sets 
my_set = {1,2,3,4}
my_set.add(22)
print(my_set)
my_set.remove(3)
print(my_set)
my_set.discard(2)
print(my_set)
my_set.pop()
print(my_set)
print(len(my_set))
print(max(my_set))
print(min(my_set))
print(sum(my_set))
print(sorted(my_set))
print(set(my_set))


set1={21,22,33}
set2={44,33,54}
result=set1.union(set2)
print(result)
result=set1.intersection(set2)
print(result)
result=set1.difference(set2)
print(result)
result=set1.symmetric_difference(set2)
print(result)
result=set1.update(set2)
print(result)
result=set1.intersection_update(set2)
print(result)
result=set1.symmetric_difference_update(set2)
print(result)
result=set1.isdisjoint(set2)
print(result)
result=set1.issubset(set2)
print(result)
result=set1.issuperset(set2)
print(result)




