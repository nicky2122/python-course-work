class details:
    def __init__(self,name,mail,password):
        self.name=name
        self._mail=mail
        self.__password=password
    def getpassword(self):#use private methods
        return self.__password
    def setpassword(self,new_password):
        self.__password=new_password 
nikhitha=details("nikhitha","nikhitha@gmail.com","nicky@21")
print(nikhitha.name)
nikhitha.name="anjali"
print(nikhitha.name)
print(nikhitha._mail)
nikhitha._mail="anjali@gmail.com"
print(nikhitha._mail)
print(nikhitha.getpassword()) 
nikhitha.setpassword("nicky@21")
print(nikhitha.getpassword)




class bank:
    def __init__(self):
        self.name="nicky"
        self._balance=0
    @property
    def noresbalance(self):
        return self._balance
    @noresbalance.setter
    def noresbalance(self,amount):
        self._balance+=amount
b=bank()
print(b.noresbalance)
b.noresbalance=2000
print(b.noresbalance)        
print(b.name)
b.name="abc"
print(b.name)



class instagram:
    def __init__(self,username,bio,account_status=False):
        self.username=username
        self._bio=bio
        self.__account_status=account_status    
    def get_acc_status(self):
        return self.__account_status
    def set_acc_status(self,status):
        self.__account_status=status 
    @property
    def bio(self):
        return self._bio  
    @bio.setter
    def bio(self,new_bio):
        self._bio=new_bio  
nicky=instagram("nicky","new ideas","False")
print(nicky.username)
nicky.username="anjali"
print(nicky.username)
print(nicky.get_acc_status())
nicky.account_status=True
print(nicky.account_status)
print(nicky.bio)
nicky.bio="i love nature"
print(nicky.bio)
