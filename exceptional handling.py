try:
    a=int(input("enter the a: "))
    b=int(input("enter the b: "))
    s=int(input("enter the string: "))
    l=[1,2,3,4]
    d={"name":"nicky","course":"python","batch":"PFS"}
    print(s)
    print(l)
    ind=int(input("enter the index: "))
    print(l[ind])
    print(d)
    key=input("enter the key: ")
    print(d[key])
    print(a+s)
    print(b+s)
    print(a/b)
except ZeroDivisionError:
    print("b cannot be Zero")
except ValueError:
    print("please enter the integer value")        
except TypeError:
    print("enter the same type")
except IndexError:
    print("enter the index with range")
except KeyError:
    print("key is not present")
else:
    print("all inputs are perfect no exceptions you can run remaining code")               