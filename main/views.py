from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

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

def blogpage(request):
    posts = Post.objects.all() 
    return render(request, 'main/blogpage.html', {'posts': posts})

def detail(request, post_id): 
    post = get_object_or_404(Post, pk=post_id) 
    return render(request, 'main/detail.html', {'post': post})

def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method == 'POST':
        new_post = Post() 
        new_post.title = request.POST['title']
        new_post.writer = request.user.username
        new_post.pub_date = request.POST['pub_date']
        new_post.content = request.POST['content']
        new_post.category = request.POST.get('category') 
        new_post.save()
        return redirect('main:detail', new_post.id)
    return redirect('main:blogpage')

def new_blog(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    return render(request, 'main/new_blog.html')

def edit(request, post_id): 
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    edit_post = get_object_or_404(Post, pk=post_id) 

    if edit_post.writer != request.user.username:
        return redirect('main:detail', edit_post.id)
    
    return render(request, 'main/edit.html', {"blog": edit_post})

def update(request, post_id): 
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    update_post = get_object_or_404(Post, pk=post_id) 

    if update_post.writer != request.user.username:
        return redirect('main:detail', update_post.id)

    if request.method == 'POST':
        update_post.title = request.POST['title']
        update_post.writer = request.user.username
        update_post.pub_date = request.POST['pub_date']
        update_post.content = request.POST['content']
        update_post.category = request.POST.get('category') 
        update_post.save()
        return redirect('main:detail', update_post.id)
    return redirect('main:detail', update_post.id)

def delete(request, post_id): 
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    delete_post = get_object_or_404(Post, pk=post_id) 

    if delete_post.writer != request.user.username:
        return redirect('main:detail', delete_post.id)

    delete_post.delete()
    return redirect('main:blogpage')

def mypage(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    my_posts = Post.objects.filter(writer=request.user.username)
    return render(request, 'main/blogpage.html', {'posts': my_posts, 'is_mypage': True})