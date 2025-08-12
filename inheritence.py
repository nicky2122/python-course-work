'''class status:
    def __init__(self,caption,image=None,video=None):
        self.caption=caption
        self.image=image
        self.vide=video
        self.videolength=30
    def see_status(self):
        if self.video:
           print(f"---{self.video}---\n'{self.caption}'")
        else:
           print(f"---{self.image}---\n'{self.caption}'")
class statusV1(status):
    def like(self):
        print("like")
    def addmusic(self,music):
        print(f"{music} music added")
nicky=statusV1("hey i'm using whatsapp","goodmrg.png")
nicky.see_status()
nicky.like()
nicky.addmusic("fear song")
nicky=statusV1("good evening","cofee.png")
nicky.see_status()
nicky.like()
nicky.addmusic("soft core")
                                                                                                                                                    
    

#types inheritence 
#single inheritence
class status:
    def uploadimage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is added to your status")
class statusV1(status):
    def addcaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is add to the status')
nicky=status()
nicky.uploadimage('prabhas.png')
anjali=statusV1()
anjali.uploadimage('selif.png')
anjali.addcaption('hii frds!!!')        


#hierarchical inheritance
class status:
    def uploadimage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is added to your status")
class statusV1(status):
    def addcaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is add to the status')
class statusV2(status):
    def like(self):
        print(f'you can like status')        
nicky=status()
nicky.uploadimage('prabhas.png')
anjali=statusV1()
anjali.uploadimage('selif.png')
anjali.addcaption('hii frds!!!')        
moksha=statusV2()
moksha.uploadimage('coffee.png')
moksha.like()


#multiple inheritence
class status:
    def uploadimage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is added to your status")
class statusV1(status):
    def addcaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is add to the status')
class statusV2(status):
    def like(self):
        print(f'you can like status')
class statusV3(statusV1,statusV2):
    def addmusic(self): 
        print(f'{self.music}...is ddded to yor status')               
nicky=status()
nicky.uploadimage('prabhas.png')
anjali=statusV1()
anjali.uploadimage('selif.png')
anjali.addcaption('hii frds!!!')        
moksha=statusV2()
moksha.uploadimage('coffee.png')
moksha.like()
anusha=statusV3
anusha.uploadimage('tress.png')
anusha.addcaption('no wifi')
anusha.like()
anusha.addmusic("radhesham.mp3")


#multi level inheritence
class status:
    def uploadimage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is added to your status")
class statusV1(status):
    def addcaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is add to the status')
class statusV2(status):
    def like(self):
        print(f'you can like status')
class statusV3(statusV1,statusV2):
    def addmusic(self): 
        print(f'{self.music}...is ddded to yor status') 
class statusV4(statusV3):
    def videolenght(self,video):
        self.video=video
        print(f'{self.video} is uploaded to your status')
                      
nicky=status()
nicky.uploadimage('prabhas.png')
anjali=statusV1()
anjali.uploadimage('selif.png')
anjali.addcaption('hii frds!!!')        
moksha=statusV2()
moksha.uploadimage('coffee.png')
moksha.like()
anusha=statusV3
anusha.uploadimage("mountains and trees.png")
anusha.addcaption("no wifi")
anusha.like()
anusha.addmusic("radhesham.mp3")
divya=statusV4
divya.uploadimage("ram.png")
divya.addcaption("i love nature")
divya.like()
divya.addmusic("ninne.mp3")
divya.videolenght("somevideo.mp4")'''

'''#super methon in inheritence
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

'''


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