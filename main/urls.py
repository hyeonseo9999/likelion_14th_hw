from django.urls import path

from . import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('second/', views.secondpage, name='secondpage'), 
    path('new/', views.new_blog, name='new_blog'), 
    path('create/', views.create, name='create'),
    path('list/', views.blogpage, name='blogpage'), 
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('update/<int:post_id>/', views.update, name='update'),
    path('delete/<int:post_id>/', views.delete, name='delete'),  
    path('mypage/', views.mypage, name='mypage'), 
    path('comment_delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('comment_edit/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('tags', tag_list, name='tag_list'),
    path('tags/<int:tag_id>', tag_post_list, name='tag_post_list'),
]