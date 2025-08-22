#super methon in inheritence
class instagram:
    def __init__(self,username):
        self.username=username
        self.post=[]
        print(f"{self.username.center(40,'-')}")
class instagramV1(instagram):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio=bio
        print(f'bio uploaded')
nicky=instagram('nicky21')
anjali=instagramV1('anjali07','coder')   


#super method 2 
class instagram:
    def __init__(self,username):
        self.username=username
        self.post=[]
        print(f"{self.username.center(40,'-')}")
    def uploadpost(self,image):
        self.image=image
        print(f'{image} is posted')    
class instagramV1(instagram):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio=bio
        print(f'bio uploaded')
    def uploadpost(self,post,music):
        super().uploadpost(post)
        self.music=music
        print(f'{self.music}is added')    
nicky=instagram('nicky21')
nicky.uploadpost("good morning.png")
anjali=instagramV1('anjali07','coder')  
anjali.uploadpost("good morning","radhesham") 




class instagram:
    def __init__(self,username):
        self.username=username
        print(f"{self.username} user is created! parent-1")
class instaV1:
    def __init__(self,username):
        self.username=username
        print(f"{self.username} user is created parent-2") 
class instaV2(instagram,instaV1):
     def __init__(self,username):
         instagram.__init__(self,username)
         instaV1.__init__(self,username)
         print(f"creating users from vesion 3")
i=instaV2("username--nicky")                      