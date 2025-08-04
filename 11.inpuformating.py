# Basic data types
a = int(input("Enter an integer: "))                          # e.g. 10
b = float(input("Enter a float: "))                           # e.g. 3.14
c = input("Enter a string: ")                                 # e.g. Hello

# List input (space-separated integers)
# Example: 1 2 3 4 5 6
d = list(map(int, input("Enter space-separated integers: ").split()))

# List input (comma-separated integers)
# Example: 1,2,3,4,5,6
e = list(map(int, input("Enter comma-separated integers: ").split(',')))

# List input (space-separated strings)
# Example: Nikitha Vishwas Gowtham Pavan
f = input("Enter names separated by space: ").split()

# List of floats
# Example: 1.3 2.4 3.2 4.5 5.23 6.12
g = list(map(float, input("Enter space-separated float numbers: ").split()))

# Any data structure using eval (list, tuple, dict, set)
# Example: [1,2,3,4] or {"name": "nikitha", "age": 21}
h = eval(input("Enter any Python structure (list, dict, etc.): "))

# Multiple values input (like user data)
# Example: xyz@1 123 @gmail.com
username, password, mail = input("Enter username, password, mail: ").split()

# Example: Gowtham 21 45
name, age, ids = input("Enter name, age, ID: ").split()

# Tuple input (comma-separated)
# Example: 1,2,3,4,5
i = tuple(map(int, input("Enter comma-separated tuple values: ").split(',')))

# Tuple input (space-separated)
# Example: 1 2 3 4 5
j = tuple(map(int, input("Enter space-separated tuple values: ").split()))

# Tuple of strings
# Example: laptop mobile banana apple
k = tuple(input("Enter space-separated items: ").split())

# Tuple of two items
# Example: xyz123 xyz@123
username, password = tuple(input("Enter username and password: ").split())

# Tuple via eval
# Example: (1, 2, 3, 4)
l = eval(input("Enter a tuple using eval: "))

# Set from space-separated values
# Example: 1 2 3 4 5
m = set(map(int, input("Enter space-separated integers for set: ").split()))

# Set from comma-separated values
# Example: 1,2,3,4,5
n = set(map(int, input("Enter comma-separated integers for set: ").split(',')))

# Set from comma-separated strings
# Example: u1,u2,u3,u4,u5
o = set(input("Enter comma-separated strings for set: ").split(','))

# Set using eval
# Example: {1,2,3,4,5}
p = eval(input("Enter set using eval: "))

# Dictionary using eval
# Example: {'name':'Nikitha', 'age': 21}
q = eval(input("Enter dictionary using eval: "))



