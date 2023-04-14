from django.shortcuts import render, redirect
from .models import Article, Comment, double_Comment
from django.utils import timezone

# Create your views here.
def new(request):
    if request.method == 'POST':
        print(request.POST)

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        return redirect('list')
    return render(request, 'new.html')

def list(request):
    hobbies = Article.objects.filter(category='hobby')
    hobbies_len = len(hobbies)

    foods = Article.objects.filter(category='food')
    foods_len = len(foods)

    programmings = Article.objects.filter(category='programming')
    programmings_len = len(programmings)

    return render(request, 'list.html', {'hobbies_len': hobbies_len, 'foods_len': foods_len, 'programmings_len': programmings_len})

def detail(request, article_id):

    article_detail = Article.objects.get(id = article_id)
    created_datetime = article_detail.datetime

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            article_detail = article_detail,
            content = content,
        )
        
        return redirect('detail', article_id)
   
    return render(request, 'detail.html', {'article_detail': article_detail, 'created_datetime':created_datetime})

def delete_comment(request, article_id, comment_id):
   comment = Comment.objects.get(pk=comment_id)
   comment.delete()
   return redirect('detail',article_id)

def double_comment(request, article_id, comment_id):
   article_detail = Article.objects.get(id=article_id)        
        
   if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        content = request.POST['content']
        
        double_Comment.objects.create(
            comment = comment, 
            content = content,
        )
        return redirect('detail',article_id)

   return render(request, 'detail.html', {'article_detail': article_detail})

def delete_double_comment(request, article_id, comment_id, double_comment_id):
   double_comment = double_Comment.objects.get(id=double_comment_id)
   double_comment.delete()
   return redirect('detail',article_id)


def category(request, category_kind):
    category_kind_templates = category_kind
    categorized_articles = Article.objects.filter(category=category_kind)

    return render(request, 'category.html', {'categorized_articles': categorized_articles, 'category_kind_templates':category_kind_templates,})