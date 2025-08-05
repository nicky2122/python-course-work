#1. List Comprehension with Numbers (int/float)
#square of numbers
square=[x**2 for x in range(1,8)]
print(square)
#only even numbers
even=[x for x in range(10) if x%2==0]
print(even)
#2. List Comprehension with Strings
# Convert to uppercase:
names=["nicky","anjli","moksha","arvindh"]
upper=[name.upper()for name in names]
print(upper)
#Get vowels from a string:
text="python programming"
vowels=[n for n in text if n in "aeiou"]
print(vowels)
#3. List Comprehension with Tuples
#Convert list of tuples to list of first elements:
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
firsts = [x[0] for x in pairs]
print(firsts)
#4. List Comprehension with Dictionaries
# Get all keys:
d = {'a': 1, 'b': 2, 'c': 3}
keys = [k for k in d]
print(keys)
# 5. List Comprehension with Sets
nums = [1, 2, 2, 3, 4, 4]
unique_squares = {x**2 for x in nums}
print(unique_squares)
#6. Nested List Comprehensions (2D List)
# Flatten a 2D list:
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)
# 7. With if-else inside comprehension
nums = [1, 2, 3, 4]
result = ['even' if x % 2 == 0 else 'odd' for x in nums]
print(result)
