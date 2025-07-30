data={
    'anjali@gmail.com':'1234',
    'nikhitha@gmail.com':'2222',
    'arvind@gmail.com':'5555',
    'moksha@gmail.com':'7777',
    }
email,password=input("enter the email and password: ").split()
if data.get(email)== password:
    print('login successfull')
else:
    print('invalid login')