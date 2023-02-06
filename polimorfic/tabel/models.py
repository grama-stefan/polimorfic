from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

    def __str__(self):
        return self.content + '|' + str(self.user)

class Post(Content):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)

class Comment(Content):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    
    



