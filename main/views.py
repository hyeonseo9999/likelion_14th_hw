from django.shortcuts import render, redirect, get_object_or_404
from .models import Post,Comment,Tag
from django.contrib.auth.models import User
from accounts.models import Profile

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

    if request.method == 'POST' and request.user.is_authenticated:
        new_comments = Comment()

        new_comments.post = post
        new_comments.writer = request.user  
        new_comments.content = request.POST['content']

        new_comments.save()
        return redirect('main:detail', post_id)
    
    comments = Comment.objects.filter(post=post)
    return render(request, 'main/detail.html', {'post': post, 'comments':comments})

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post_id = comment.post.id 
    if comment.writer == request.user:
        comment.delete()
    return redirect('main:detail', post_id)

def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        comment.content = request.POST['content']
        comment.save()
        return redirect('main:detail', comment.post.id)
    return render(request, 'main/comment_edit.html', {'comment': comment})

def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method == 'POST':
        new_post = Post() 
        new_post.title = request.POST['title']
        new_post.writer = request.user
        new_post.pub_date = request.POST['pub_date']
        new_post.content = request.POST['content']
        new_post.category = request.POST.get('category') 

        new_post.save()

        save_tags(new_post)

        return redirect('main:detail', new_post.id)
    

def new_blog(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    return render(request, 'main/new_blog.html')

def edit(request, post_id): 

    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    edit_post = get_object_or_404(Post, pk=post_id) 

    if edit_post.writer != request.user:
        return redirect('main:detail', edit_post.id)
    
    return render(request, 'main/edit.html', {"blog": edit_post})

def update(request, post_id): 
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    update_post = get_object_or_404(Post, pk=post_id) 

    if update_post.writer != request.user:
        return redirect('main:detail', update_post.id)

    if request.method == 'POST':
        update_post.title = request.POST['title']
        update_post.writer = request.user
        update_post.pub_date = request.POST['pub_date']
        update_post.content = request.POST['content']
        update_post.category = request.POST.get('category') 

        update_post.save()

        save_tags(update_post)

        return redirect('main:detail', update_post.id)

def delete(request, post_id): 
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    delete_post = get_object_or_404(Post, pk=post_id) 

    if delete_post.writer != request.user:
        return redirect('main:detail', delete_post.id)

    delete_post.delete()
    return redirect('main:blogpage')

def mypage(request, id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    profile_user = get_object_or_404(User, pk=id)
    profile = get_object_or_404(Profile, user=profile_user)
    my_posts = profile_user.post_set.all()
    is_mypage = (request.user == profile_user)

    return render(request, 'users/mypage.html', {'profile_user': profile_user,'posts': my_posts, 'is_mypage': is_mypage, 'profile': profile})

def save_tags(post):
    words = post.content.split()
    tag_list = []

    for w in words:
        if len(w) > 0:
            if w[0] == '#':
                tag_list.append(w[1:])

    post.tags.clear()

    for t in tag_list:
        tag, boolean = Tag.objects.get_or_create(name=t)
        post.tags.add(tag)

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'main/tag_list.html', {'tags' : tags})

def tag_post_list(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    posts = tag.posts.all()
    return render(request,'main/tag_post_list.html', {'tag':tag, 'posts':posts})

def likes(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()

    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
    return redirect('main:detail', post.id)

def comment_likes(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user in comment.comment_like.all():  
        comment.comment_like.remove(request.user)
        comment.comment_like_count -= 1
        comment.save()

    else:
        comment.comment_like.add(request.user)
        comment.comment_like_count += 1
        comment.save()
    return redirect('main:detail', comment.post.id)    
