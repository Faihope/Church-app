
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField( upload_to='images_uploaded',null=True)
    video=models.FileField( upload_to='images_uploaded',null=True)
    content=models.TextField()  

    def __str__(self):
        return self.title

class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=500,default='')
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering=('created',)

    def __str__(self):
        return 'Coment by {} on {}'.format(self.name)