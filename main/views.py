from django.shortcuts import render

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