from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    article_list = Article.objects.all()
    # Paginator
    # 1. articles를 Paginator에 입력
    paginator = Paginator(article_list, 3)
    # 2. 몇번째 page를 보여줄건지 GET으로 가져옴
    page = request.GET.get('page')
    # 3. 해당하는 page의 articles만 뽑기
    articles = paginator.get_page(page)
    # 4. 총 page 수를 range로 변환
    # num_pages = range(1, articles.paginator.num_pages() + 1)

    context = {
        'articles' : articles,
        # 'num_pages' : num_pages,
    }
    return render(request, 'articles/index.html', context)  # articles-templates-articles-index.html


# Form 사용
# def new(request):
#     if request.method == 'POST':
#         # 데이터베이스에 데이터 생성
#         # 1. 넘어온 데이터를 받기
#         article_form = ArticleForm(request.POST)
#         # title = request.POST.get('title')
#         # content = request.POST.get('content')
#         # 2. 넘어온 데이터 검증
#         if article_form.is_valid():  # 데이터가 유효한지 검증
#             title = article_form.cleaned_data.get('title')
#             content = article_form.cleaned_data.get('content')
#             # 3. 데이터베이스에 article 만들기
#             article = Article.objects.create(title=title, content=content)
#             # 4. redirect -> detail (detail->상세 페이지 보여주기, 동적으로 바뀌는 페이지, pk에 바뀌는 페이지에 대한 숫자 넣어주기)
#             return redirect('articles:detail', article.pk)  # redirect 함수 추가해야함
#     else:
#         article_form = ArticleForm()
#         # 폼을 보여줌
#         context = {
#             'article_form' : article_form,
#         }
#         return render(request, 'articles/new.html', context)



@login_required # 로그인이 안되어있어도 주소를 입력하면 articles/new 페이지로 직접 갈 수 있는데 이거 못가게 막는 것 
# ModelForm 사용
def new(request):
    if request.method == 'POST':
        # 데이터베이스에 데이터 생성
        # 1. 넘어온 데이터를 받기
        article_form = ArticleForm(request.POST)
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # 2. 넘어온 데이터 검증
        if article_form.is_valid():  # 데이터가 유효한지 검증
            # 3. 데이터베이스에 article 만들기
            article = article_form.save(commit=False)  # form 사용했을 때 if문 안쪽의 3줄의 코드가 -> modelform을 사용하면 한줄로 줄어든다.
            # 3-1. user 정보 끼워넣기
            article.user = request.user
            article.save()
            # 4. redirect -> detail (detail->상세 페이지 보여주기, 동적으로 바뀌는 페이지, pk에 바뀌는 페이지에 대한 숫자 넣어주기)
            return redirect('articles:detail', article.pk)  # redirect 함수 추가해야함
    else:
        article_form = ArticleForm()
    # 폼을 보여줌 : else에서 빼줌 -> is_valid가 성립하지 않을때 보여줄 수 있음. 문법적인 오류 발생안함.
    # 화면에서 F12 눌러서 네모칸(타이틀, 텍스트 입력하는 칸)에 가서 'required id = ~~ ' 이 부분을 삭제하고, 빈칸으로 제출을 누르면
    # 이 입력란을 작성하라고 뜨거나 필수항목이라고 뜬다 (유효성 검증)
    context = {
        'article_form' : article_form,
    }
    return render(request, 'articles/new.html', context)


def detail(request, pk):
    # 1. pk번째 데이터를 가져오기
    article = Article.objects.get(pk=pk)
    # 2. context로 넘겨주기
    context = {
        'article' : article,
    }
    # 3. render와 함께 넘겨주기
    return render(request, 'articles/detail.html', context) 


# form 사용
# def edit(request, pk):
#     article = Article.objects.get(pk=pk)  # 수정하고자 하는 게시물의 정보가 들어있음
#     if request.method == 'POST':
#         # article 수정
#         # 1. 넘어온 데이터 받기
#         article_form = ArticleForm(request.POST)
#         # 2. 데이터 검증
#         if article_form.is_valid():
#             article.title = article_form.cleaned_data.get('title')
#             article.content = article_form.cleaned_data.get('content')
#             article.save()
#             # 4. redirect -> detail
#             return redirect('articles:detail', article.pk)
#     else:
#         # article 수정하는 form 보여주기(=render)
#         article_form = ArticleForm(
#             {
#                 'title' : article.title,
#                 'content' : article.content,
#             }
#         )
#         context = {
#             'article_form' : article_form,
#         }
#         return render(request, 'articles/new.html', context)


@login_required
# MdelForm 사용
def edit(request, pk):
    article = Article.objects.get(pk=pk)  # 수정하고자 하는 게시물의 정보가 들어있음
    # article의 주인인지 검증
    if request.user != article.user:
        return redirect('articles:index')
    
    if request.method == 'POST':
        # article 수정
        # 1. 넘어온 데이터 받기 
        article_form = ArticleForm(request.POST, instance=article)  # 인스턴스를 넘겨주면서 데이터 받을 때 수정도 같이 해버림
        # 2. 데이터 검증
        if article_form.is_valid():
            # 3. 검증된 데이터로 수정 & 저장
            article_form.save()  # 수정한거를 저장(실제 수정은 1번에서 수정)
            # 4. redirect -> detail
            return redirect('articles:detail', article.pk)
    else:
        # article 수정하는 form 보여주기(=render)
        article_form = ArticleForm(instance=article)  # pk로 가져온 하나의 게시물을 인스턴스에 넣어준다
    context = {
        'article_form' : article_form,
    }
    return render(request, 'articles/new.html', context)


# POST 요청만 받음
@login_required
def like(request, pk):
    # 1. pk번 article을 가져오기
    article = Article.objects.get(pk=pk)
    # 2. 현재 로그인한 user가 이 article에 좋아요를 눌렀는지 판별
    if request.user in article.like_users.all():
        # 3-1. 좋아요 취소
        article.like_users.remove(request.user)
    else:    
        # 3-2. 좋아요
        article.like_users.add(request.user)

    return redirect('articles:detail', pk)


# GET 요청을 받음, 검색페이지
def search(request):
    # 1. request로부터 검색어 가져오기
    query = request.GET.get('query') # -> asdf
    # 2. article에서 제목에 검색어가 있는지 찾기
    articles = Article.objects.filter(title__contains=query)  # title에 이 query가 있는 친구들만 가져와
    # title__contains : 대소문자 구분 안함(A 입력해도 a 나와영)
    # title__icontains : 대소문자 구분 해서 검색(A 입력하면 A만 나옴) -> 근데 지금은 안됨...
    # 고급 검색기능을 하고 싶으면 별도의 검색 엔진을 사용해야하는데, solr(솔라) 대표적 -> 이런건 검색엔진 서버를 따로 돌려야함(장고 서버 돌리고 검색엔진도 서버 돌리고..)
    # but 기본적인 간단한 기능은 장고에 다 있음..!!!
    # 3. context로 결과값 template에 넘겨주기
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/search.html', context)