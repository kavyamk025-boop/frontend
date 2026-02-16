from models.post import Post
from services.notification import PushNotification

class User:
    def __init__(self,username:str,email:str):
        self.username=username
        self._email=email
        self.posts=[]
        self.followers=[]
    def create_post(self,content:str):
        post=Post(self,content)
        self.posts.append(post)
        return post
    def follow(self,user:"user"):
        user.followers.append(self) 
    def get._email(self):
           return self._email 

class CreatorUser(User):
     def create_post(self,content:str):
          post=super()create.post(content)

        for follower in self.followers:
          notifier=PushNotification()
          notifier.send(f"{self.username}posted now content")
          
          return post          