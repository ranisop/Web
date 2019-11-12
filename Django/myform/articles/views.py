from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
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
            article = article_form.save()  # form 사용했을 때 if문 안쪽의 3줄의 코드가 -> modelform을 사용하면 한줄로 줄어든다.

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


# MdelForm 사용
def edit(request, pk):
    article = Article.objects.get(pk=pk)  # 수정하고자 하는 게시물의 정보가 들어있음
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