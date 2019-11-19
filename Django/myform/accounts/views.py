from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm  # 유저생성(회원가입)폼, 인증(로그인할때)폼, 유저변경폼, 비밀번호변경폼
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash


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
            # 4-1. 주소창에 next값이 있으면 next로 redirect하고, 없으면 articles:index로 redirect하라.
            next = request.GET.get('next') # 주소창에 있는 값은 POST가 아니라 GET으로 받아야 함
            return redirect(next or 'articles:index')
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


def password(request):
    if request.method == 'POST':
        # 실제로 비밀번호 변경
        # 1. 넘어온 데이터 Form에 입력
        form = PasswordChangeForm(request.user, request.POST)  # POST로 넘어온 바꾸고자 하는 비밀번호의 데이터를 원래 유저의 정보에다가 넣어주기
        # 2. 검증
        if form.is_valid():
            # 3. 비밀번호 저장
            user = form.save()  # 새 비밀번호가 저장되면 세션이 만료가 되면서 다 로그아웃됨
            # 3-1. 세션 유지(지금 비밀번호 바꾼 브라우져는 user이기 때문에 그 창은 로그아웃이 되지 않도록 세션 유지하기)
            update_session_auth_hash(request, user)
            # 4. redirect -> 메인 페이지
            return redirect('articles:index')
    else:
        # 비밀번호를 변경하는 양식 보여줌
        form = PasswordChangeForm(request.user)  # 어떤 유저의 비밀번호를 변경할건지 알아야하기 때문에 꼭 유저 정보가 담긴 파라미터를 넣어줘야함
    
    context = {
        'form' : form,
    }
    return render(request, 'accounts/password.html', context)






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