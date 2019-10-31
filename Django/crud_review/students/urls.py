'''
원래 urls.py에서 틀 가져오기
from django.urls import path

urlpatterns = [
   
]
'''


from django.urls import path
from . import views  # 같은 폴더에서 views를 import 해와라

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'),  # GET /students/
    path('new/', views.new, name='new'),  # views가 없으니까 위에 임포트 해죠야해  # GET /students/new/
    # new + create 하려고 create 없앰  # GET,POST /students/new/
    #path('create/', views.create, name='create'),  # POST /students/create/
    path('<int:pk>/', views.detail, name='detail'),  # GET /students/1/
    path('<int:pk>/edit/', views.edit, name='edit'),  # 뭐를 수정할지 알려줘야 하니까 <int:pk>/를 같이 넣어야해  # GET students/1/edit/
    # edit + update  # GET,POST students/1/edit/
    #path('<int:pk>/update/', views.update, name='update'),  # GET /students/1/update/ (x)
    path('<int:pk>/delete/', views.delete, name='delete'),  # GET /students/1/delete/ (x)

]

#
# 😀URL Name -> 각각의 패스에 적용

# path('주소/', views.함수, name='이름')
# django templates language : {{ }} or {% %}
# {% url '이름' %} => 주소로 바로 변환
# ex) {% url 'new' %} => /students/new/  # index.html 페이지에서 사용

# [장점]
# 1. 주소의 변경이 필요할 때, urls.py에서만 수정해주면 됨
#   - urls.py는 url 주소를 관리하는 페이지인데 name을 사용하지 않고 링크 입력하는 방법으로 사용하면
#   - 주소가 변경될 때 이 주소가 변경되는 html을 모두 찾아서 수정해야하는 번거로움이 있음
# 2. 마지막 '/'를 빼먹는 실수를 차단 가능

# App Name -> 특정 app의 urls.py에 적용
# {% url '앱이름:패스이름' %} = {% url 'app_name:path_name' %}
# {% url 'students:index' %}


#
# 😀RESTful
# 1. 자원(Resource) - URI
# 2. 행위(Verb) - http method (GET, POST, ...)
# 3. 표현(Representations) = 자원 + 행위
# 예)
# GET/users/read/1 (x)  -> read 같이 주소 안에 행위가 들어가면 restful한 주소가 아님
# GET/users/1 (o)

# restful 기본
# 1) 슬래시(/)는 개층 관계를 나타내는데 사용
# 2) 소문자 사용
# 3) 파일 확장자는 포함 안함
# 4) 밑줄(_) 대신 하이픈(-) 사용
# 5) 주소 마지막에 슬래시(/)를 포함하지 않음 -> django는 끝에 필수로 포함해야 하는 경우도 있어서 헷갈림


# Django는 PUT/PATCH/DELETE 불가능, 따라서..
# GET  /studetns/2/edit  #=> 수정 페이지 보여줌
# POST /students/2/edit  #=> 수정 작업 수행
# ex)
# GET    /users/1  #=> user 1번 가져옴
# PUT    /users/1  #=> user 1번 수정
# DELETE /users/1  #=> user 1번 삭제

