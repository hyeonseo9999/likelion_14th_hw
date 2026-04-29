from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:blogpage')
        else:
            return render(request, 'accounts/login.html', {'error': '아이디 또는 비밀번호가 일치하지 않습니다.'})
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:blogpage')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            username = request.POST['username']
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/signup.html', {'error': '이미 존재하는 아이디입니다.'})
            
            newuser = User.objects.create_user(
                username=username,
                password=request.POST['password'],
            )

            nickname = request.POST['nickname']
            major = request.POST['major']
            introduction = request.POST.get('introduction', '')
            profile_image = request.FILES.get('profile_image')

            profile = Profile(
                user=newuser,
                nickname=nickname,
                major=major,
                introduction=introduction,
                profile_image=profile_image,
            )
            profile.save()

            auth.login(request, newuser)
            return redirect('main:blogpage')
        
        else:
            return render(request, 'accounts/signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
                            
    return render(request, 'accounts/signup.html')