from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm  # 유저생성(회원가입)폼, 인증(로그인할때)폼, 유저변경폼
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm

# Create your views here.
def signup(request):
    # 로그인이 되어 있으면 회원가입 실행하지 않기(로그인 유무 판별 & 로그인 된 경우 redirect)
    if request.user.is_authenticated:  # 로그인이 되어있다면 True, 아니면 False
        return redirect('articles:index')

    if request.method == 'POST':
        # 실제 회원 생성
        # 1. 넘어온 데이터르러 Form Class에 입력하기
        form = UserCreationForm(request.POST)
        # 2. 유효한 값인지 검증하기
        if form.is_valid():
            # 3. 회원 생성
            user = form.save()
            # 3-1. 로그인
            auth_login(request, user)
            # 4. redirect => 메인 페이지 (articles index)
            return redirect('articles:index')
    else:
        # 회원 가입 양식 보여줌
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)  # signup 페이지 보여주기


def login(request):
    # 로그인이 되어 있으면 로그인페이지 다시 보여주지 않기
    if request.user.is_authenticated:  # 로그인이 되어있다면 True, 아니면 False
        return redirect('articles:index')

    if request.method == 'POST':
        # 로그인
        # 1. POST 요청으로 넘어온 데이터를 Form에 입력
        form = AuthenticationForm(request, request.POST)  # request.POST : 사용자가 입력한 로그인 정보(아이디, 비번)를 가지고 있음, 이걸로 검증하는것
        # 2. 검증
        if form.is_valid():
            # 3. 로그인 수행
            auth_login(request, form.get_user())  # form.get_user() : 메소드, 검증을 통과한 유저의 정보가 담겨있음.
            # 4. redirect => 메인 페이지 (articles index)
            return redirect('articles:index')
    else:
        # 로그인 창 보여줌
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)  # login 창 보여주기


# POST 요청을 받음
def logout(request):
    if request.method == 'POST':
        # 로그아웃 수행
        auth_logout(request)
        return redirect('articles:index')  # 메인페이지 보여줌


def edit(request):
    if request.method == 'POST':
        # 회원 정보 수정
        # 1. POST로 넘어온 데이터 Form에 입력
        form = CustomUserChangeForm(request.POST, instance=request.user)
        # 2. 검증
        if form.is_valid():
            # 3. 저장
            form.save()
            # 4. redirect -> 메인(articles index)
            return redirect('articles:index')
    else:
        # 회원 정보 수정 Form 보여줌
        form = CustomUserChangeForm(instance=request.user) # 현재 로그인한 유저의 정보가 폼에 자동으로 채워짐, UserChangeForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/edit.html', context)


def delete(request):
    if request.method == 'POST':
        # user 삭제
        request.user.delete()
        return redirect('articles:index')



# Sign Up vs. Login
# 1. Signup
# user를 Create

# 2. Login
# Session에서 User 정보를 Create(생성 보다는 담아놓는, 임시로 들고있는)

# 3. Logout
# Session에서 User 정보를 Delete

# Session이란?
# Django가 브라우져의 정보를 가져와 임시로 들고 있도록 해서
# 지금 이 페이지를 보는 User가 누구인지 서버쪽에서 정보를 들고 있는 것.
# ex) 쇼핑몰 장바구니에 여러가지 담아놓고, 브라우져를 껐다 켜면 장바구니 그대로 유지 -> 세션이라는 곳에 정보를 담아놔서 가능!
# Django에서는 Session을 이용해서 이런 기능 사용할 수 있음.