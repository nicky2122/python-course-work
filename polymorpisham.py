#method overriding
class normaluser:
    def playvideo(self,name):
        print(f"\n{name} is playing video with:\n1.normal quality\n2.ads run\n3.no background\n4.limited videos download\n4.music with ads")
    def like(self):
        pass
    def comments(self):
        pass
    def title(self):
        pass
    def share(self):
        pass
    def description(self):
        pass
    def subsribe(self):
        pass
class premiumuser(normaluser):
    def playvideo(self,name):
        print(f"\n{name} is playing video with:\n1.high quality\n2.ads free\n3.background play\n4.downloading\n5.exclusive music")  
nicky=normaluser()
anjali=premiumuser()
nicky.playvideo("nicky")
anjali.playvideo("anjali")        

#
class normaluser:
    def play_video(self,name):
        print(f"\n{name} is playing video with:\n1.normal quality\n2.ads run\n3.no background\n4.limited videos download\n4.music with ads")
    
class premiumuser(normaluser):
    def play_video(self,name):
        print(f"\n{name} is playing video with:\n1.high quality\n2.ads free\n3.background play\n4.downloading\n5.exclusive music")  
def play_video(user,username):
    user.play_video(username)

nicky=normaluser()
anjali=premiumuser()
moksha=premiumuser()
arvindh=normaluser()
sandeep=premiumuser()
jashuva=normaluser()

nicky.play_video("nicky")
anjali.play_video("anjali")        
moksha.play_video("moksha")
arvindh.play_video("arvindh")
sandeep.play_video("sandeep")
jashuva.play_video("jashuva")


# operator overloading
class number:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n+other.n
    def __sub__(self,other):
        return self.n-other.n
    def __mul__(self,other):
        return self.n*other.n
    def __str__(self):
        return f"{self.n}"
    def __lt__(self,other):
        return self.n<other.n
    def __gt__(self,other):
        return self.n>other.n
    def __ed__(self,other):
        return self.n==other.n
number1=number(10)
number2=number(20)
print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1)
print(number1<number2)
print(number1>number2)
print(number1==number2)

