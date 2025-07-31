
a=55
b=20
print("addition:",a+b)#addition: 75
print("subtraction:",a-b)#subtraction: 35
print("multiply:",a*b)#multiply: 1100
print("division:",a/b)#division: 2.75
print("floor division:",a//b)#floor division: 2
print("modulus:",a%b)#modulus: 15
print("exponentiation:",a**b)#exponentiation: 64158439152961731834506988525390625


#comparison operators
c=10
d=40
print("equal to(==):",c==d)#equal to(==): False
print("not equal to(!=):",c!=d)#not equal to(!=): True
print("greater than(>):",c>d)#greater than(>): False
print("lessthan(<):",c<d)#lessthan(<): True
print("greaterthan or equal to(>=):",c>=d)#greaterthan or equal to(>=): False
print("lessthan or equal to(<=):",c<=d)#lessthan or equal to(<=): True


#assign operator
'''
var=var(op)(var)
e=e+10
var(op)=var
e+=10
'''
a=40
a+=60
print("assign & add(+=):",a)#assign & add(+=): 100
a-=3
print("assign & sub(-=):",a)#assign & sub(-=): 97
a*=4
print("assign & multiply(*=):",a)#assign & multiply(*=): 388
a/=5
print("assign & division(/=):",a)#assign & division(/=): 77.6
a//=5
print("assign & floor division(//=):",a)#assign & floor division(//=): 15.0
a%=2
print("assign & modulus(%=):",a)#assign & modulus(%=): 1.0
a**=3
print("assign & exponentional(**=):",a)#assign & exponentional(**=): 1.0


#logical operator
'''
=====AND=====
T AND T = T
T AND F = F
F AND T = F
F AND F = F

(T AND T AND T AND T) = T{ALL ARE TRUE THEY ARE TRUE}
(T AND T AND T AND F) = F{THEY WAS ONE FALSE THAT CONDITION WILL BE FALSE}

=====OR======
T OR T = T
T OR F = T
F OR T = T
F OR F = F

(T OR T OR T OR T) = T
(T OR T OR T OR F) = T{THEY WILL BE ONE TRUE THAT CONDITION WILL BE TRUE}

=====NOT======

NOT T = F
NOT F = T
'''
a=30
b=60
print("and:",a%10==0 and b%10==0)#and: True
print("or:",a%4==0 or b%4==0)#or: True
print("not:",not a%7==0)#not: True


#membership operator
names=("nicky","anjali","moksha","arvind")
print("in result:",'nicky' in names)#in result: True
print("not in result:",'yogamma' in names)#not in result: False

#identity operator
x=[1,2,3,4]
y=[7,8,9,6]
a=x#assign a to x
print("x is y:",x is y)#x is y: False
print("x is a:",x is a)#x is a: True
print("id(x):",id(x))#id(x): 2293440858048
print("id(y):",id (y))#id(y): 2293440858496
print("id(a):",id(a))#id(a): 2293440858048
print("a is not x:",a is not x)#a is not x: False
print("x is not y:",x is not y)#x is not y: True

#bitwise operator
'''
1-001
2-010
3-011
4-100
5-101
6-110
7-111

3-011      4=100
5-101      7=111
------
3&5=001=1   4&7=100=4

4-100       4=100
5-101       7=111
-------
4/5=101=5    4/7=111=7

5-101        4=100
6-110        7=111
-------      
5^6=011=3    4^7=011=3

1-001        4=100
-------
~1=110=6     ~4=011=3

2<<1
2=010
4=100

4>>1
4=100
2=010
'''
x=4
y=6
print("and x&y:",x&y)#and x&y: 4
print("or x/y:",x/y)#or x/y: 0.6666666666666666
print("not ~x:",~x)#not ~x: -5
print("liftshift x<<y:",x<<y)#liftshift x<<y: 256
print("rightshift x>>y:",x>>y)#rightshift x>>y: 0
print("xor x^y:",x^y)#xor x^y: 2



