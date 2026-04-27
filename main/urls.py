from django.urls import path

from . import views
from .views import *

app_name = 'main'
urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('second', secondpage, name='secondpage'),
    path('new_blog', new_blog, name='new_blog'),
    path('create', create, name='create'),
    path('blog', blogpage, name='blogpage'),
    path('detail/<int:blog_id>', detail, name='detail'),
    path('edit/<int:blog_id>', edit, name='edit'),
    path('update/<int:blog_id>', update, name='update'),
    path('delete/<int:blog_id>', delete, name='delete'),  
]