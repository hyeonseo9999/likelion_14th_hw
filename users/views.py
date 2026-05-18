from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from accounts.models import Profile
from django.shortcuts import redirect

def mypage(request, id):
    profile_user = get_object_or_404(User, pk=id)
    profile =  get_object_or_404(Profile, user=profile_user)

    context = {
        'profile_user':profile_user,
        'profile': profile,
    }

    return render(request, 'users/mypage.html', context)

def follow(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower=user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)