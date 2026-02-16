class post:
    def __init__ (self,author,content:str):
        self.author=author
        self.content=content
        self.likes=[]
    def like(self,user):
        if user.username not in self.likes:
            self.likes.append(user.username)
    def display(self):
        print(f"{self.author.username}:{self.content}")
        print(f"likes:{len(self.likes)}")            