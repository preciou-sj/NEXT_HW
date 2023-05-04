from django.contrib import admin
from .models import Comment, Post

model = Comment

@admin.register(Post) 
 
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'title', 'author']
    
    list_display_links = ['id', 'title']
   
    list_filter = ['author'] 
 
    search_fields = ['title', 'author']
  

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'content', 'author')
