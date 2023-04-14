from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=30)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
   article_detail = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
   content = models.TextField()

class double_Comment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='double_comments')
    content = models.TextField()


    def __str__(self):
       return self.content
