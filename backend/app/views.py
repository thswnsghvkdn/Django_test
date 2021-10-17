from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Notice , Notice3

# Create your views here.
def join(request):
    if request.method == "POST" : # 정보를 넘긴 경우
        name = request.POST['username']
        pw = request.POST['password']

        # 중복검사 알고리즘 여기다 넣으세요

        User.objects.create_user(username=name , password = pw) # 유저 생성

        return redirect('/') # 위치에서 template 은 생략        
    else : # 회원가입 페이지에 그냥 접속한 경우
        return render(request , 'frontend/join.html' ,{'app' : '안녕'}) # 위치에서 template 은 생략


def home(request) :
    contents = Notice.objects.filter() # 전체를 다 가져오는 방법1
    # contents = Notice.objects.all() # 전체를 다 가져오는 방법2
    # Notice.objects.filter( title = "2" )
    # contents = Notice.objects.exclude( username = "a") a 만 제외
    # contents = Notice.objects.all()[:3] 3개만 출력
    # contents = Notice.objcets.filter(username = "b").order_by("title")[:3]
    return render(request , 'frontend/notice.html' , {'contents' : contents})

def login(request) :
    # 로그인검사 
    u = request.user # 없으면 익명으로 뜸
    
    if request.method=="POST":
        name = request.POST['username']
        pw = request.POST['password']

        #맞는지 아닌지 확인
        # user 가 요청된 정보와 맞는 객체가 있는지 확인
        user = auth.authenticate(request , username = name , password = pw) 

        if user is None :
            message = "아이디가 없음"
            return render(request , 'frontend/login.html', {"message" : message})
        else : 
            auth.login(request , user) # 로그인 후 마이페이지를 보여주거나 함 역할 머야 .. 
            return redirect("/")
    else : # 로그인 되어 있는지 검사
        if str(u) == "AnonymousUser": 
            return render(request , "frontend/login.html")
        else : # 로그인 되어 있으면 로그인 페이지 접근 못함
            return redirect("/")

def logout(request):
    auth.logout(request)
    return redirect("/")


def write(request):
    if request.method == "POST" :
        t = request.POST["title"]
        c = request.POST["board"]
        u = request.user.username # 유저네임 저장
        Notice.objects.create(title=c , content = c , username = u) # 모델생성
        return redirect("/")
    else : 
        u = request.user.username
        return render(request , "frontend/writer.html" , {"username" : u })


def update(request , pk):
    contents = get_object_or_404(Notice , pk=pk)
    if request.method == "POST" :
        contents.title = request.POST["title"]
        contents.content = request.POST["board"]
        contents.save()
        return redirect("/")
    else :
        return render(request , "frontend/update.html" , {"contents" : contents} )

def delete(request, pk):
    if request.method == "POST" :
        Notice.objects.get(pk=pk).delete()
    return redirect("/")


def home_image(request) :
    contents = Notice3.objects.filter() # 전체를 다 가져오는 방법1
    # contents = Notice.objects.all() # 전체를 다 가져오는 방법2
    # Notice.objects.filter( title = "2" )
    # contents = Notice.objects.exclude( username = "a") a 만 제외
    # contents = Notice.objects.all()[:3] 3개만 출력
    # contents = Notice.objcets.filter(username = "b").order_by("title")[:3]
    return render(request , 'frontend/notice_image.html' , {'contents' : contents})

def write_image(request):
    if request.method == "POST" :
        t = request.POST["title"]
        c = request.POST["board"]
        u = request.user.username # 유저네임 저장
        i = request.FILES["images"]
        Notice3.objects.create(title=t , content = c , username = u , images = i) # 모델생성
        return redirect("/homeImage")
    else : 
        u = request.user.username
        return render(request , "frontend/writer_image.html" , {"username" : u })


def update_image(request , pk):
    contents = get_object_or_404(Notice3 , pk=pk)
    return render(request , "frontend/update_image.html" , {"contents" : contents} )

def delete_image(request, pk):
    if request.method == "POST" :
        Notice3.objects.get(pk=pk).delete()
        return redirect("/homeImage")


