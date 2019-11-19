from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),  # 빈 주소를 넣으면 http://127.0.0.1:8000/articles/
    path('new/', views.new, name='new'),  # /articles/new/
    path('<int:pk>/', views.detail, name='detail'),  # /articles/1/ or articles/2/
    path('<int:pk>/edit/', views.edit, name='edit'),  # /articles/edit/
    path('<int:pk>/like/', views.like, name='like'),
    path('search/', views.search, name='search'), # 검색페이지
]
