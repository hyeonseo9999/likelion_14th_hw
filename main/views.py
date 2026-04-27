from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def mainpage(request):
    context = {
        'generation': 14,                   
        'info': {                           
            'mainpage': 'View 작성 및 URL 연결',
            'secondpage': 'Mainpage 작성과 동일',
            'etc': 'Template 상속을 통한 중복되는 부분 분리, navbar 분리 학습 및 CSS, image 적용 학습'
        }
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    return render(request, 'main/secondpage.html')

def new_blog(request):
    return render(request, 'main/new_blog.html')

def create(request):
    new_blog = Blog()

    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = request.POST['pub_date']
    new_blog.content = request.POST['content']
    new_blog.category = request.POST['category']

    new_blog.save()

    return redirect('main:detail', new_blog.id)

def blogpage(request):
    blogs = Blog.objects.all()
    return render(request, 'main/blogpage.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'main/detail.html', {'blog': blog})

def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'main/edit.html', {"blog": edit_blog})

def update(request, blog_id):
    update_blog = get_object_or_404(Blog, pk=blog_id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.pub_date = request.POST['pub_date']
    update_blog.content = request.POST['content']
    update_blog.category = request.POST['category']
    update_blog.save()

    return redirect('main:detail', update_blog.id)

def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()

    return redirect('main:blogpage')