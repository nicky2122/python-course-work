#Syntax of a Dictionary:
d={'k1':'v1','k2':'v2'}
#examples
student={'name':'nicky','branch':'cse','age':21}
print(student)
#2. Dictionary Operations
#2.1 Accessing Values
student={'name':'nicky','branch':'cse','age':21}
print(student['name'])
print(student.get('age'))
#2.2 Adding and Updating Items
student={'name':'nicky','branch':'cse','age':21}
student['age']=22
student['city']='ap'
print(student)
#2.3 Removing Items from a Dictionary
student={'name':'nicky','branch':'cse','age':21}
age=student.pop('age')
print(student)
del student['branch']
print(student)
student.popitem()
print(student)
student.clear()
print(student)


#3. Dictionary Built-in Methods
#3.1 Dictionary Methods for Accessing Data
student={'name':'nicky','branch':'cse','age':21}
print(student.get('name'))
print(student['branch'])
print(student.values())

