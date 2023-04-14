"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new', views.new, name='new'),
    path('list', views.list, name='list'),
    path('detail/<int:article_id>', views.detail, name='detail'),
    path('category/<str:category_kind>', views.category, name='category'),
    path('delete-comment/<int:article_id>/<int:comment_id>',views.delete_comment, name='delete-comment'),
    path('delete_double_comment/<int:article_id>/<int:comment_id>/<int:double_comment_id>',views.delete_double_comment, name='delete_double_comment'),
    path('double_comment/<int:article_id>/<int:comment_id>',views.double_comment, name='double_comment'),
]
