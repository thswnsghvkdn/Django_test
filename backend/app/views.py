from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth

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
    return render(request , 'frontend/notice.html')

def login(request) :
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
    else :
        return render(request , "frontend/login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")