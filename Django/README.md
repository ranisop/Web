# Django

1. Django 폴더 안으로 이동
2. 프로젝트 만들기
    - django-admin startproject 프로젝트이름
3. 해당 프로젝트 폴더 안으로 이동
    - 프로젝트 안에서부터는 python manage.py 명령어를 이용하여 작업
4. 앱폴더 만들기
    - python manage.py startapp 앱이름
5. 서버 실행
    - python manage.py runserver
6. setting.py 수정
    - INSTALLED_APPS = [앱이름,] → [] 안에 앱이름 추가하기
    - LANGUAGE_CODE = 'ko-kr'
    - TIME_ZONE = 'Asia/Seoul' 
7. ulrs.py 추가
    - # from 앱이름 import views
8. views.py에 코드 작성
    - Flask의 app.py와 같은 역할


$ cd web/django
$ django-admin startproject crud
$ cd crud
$ python manage.py startapp articles
$ python manage.py runserver
--
setting.py 수정
urls.py 추가
    - from django.urls import path, include 
    - path('articles/', include('articles.urls'))
crud/crud/templates 폴더 생성 후 base.html 파일 생성
    - body 안에 추가
        {% block body %}
        {% endblock %}
crud/articles/urls.py 생성 후 내용 입력
    - urlpatterns = [path('', views.index),] 만 입력
crud/articles/views.py 수정
--
~/web/django/crud 에서
$ python manage.py makemigrations 하고 아래와 같이 나오면 성공
    Migrations for 'articles':
    articles/migrations/0001_initial.py
        - Create model Article
$ python manage.py migrate
$ python manage.py shell (shell 들어가기)
    - from articles.models import Article  
        # Article에 있는 models 불러오기     
    # create




# CRUD Review

1. app 등록
2. 언어 & 시간대 설정
3. urls 파일 분리
4. template 폴더 구조 정리
5. base.html 설정
6. models.py 모델 생성
    - Student(name, age, created_at, updated_at)
7. CRUD
    - Create(new, create)
    - Read(index, detail)
    - Delete(delete)
    - Update(edit, update)


