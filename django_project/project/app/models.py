from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
   title = models.CharField(verbose_name='TITLE', max_length=50)
   content = models.TextField()
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)

   class Meta:   
        verbose_name = 'post' 
        verbose_name_plural = 'posts'

def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse(f'app:post_detail', args=[self.id])

   
class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
   content = models.TextField()
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')


   def __str__(self):
        return f'{self.author}-{self.content}'
