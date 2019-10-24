"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

# url작성법 : 앞에는 / 없이, 뒤에는 꼭 / 넣기
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),  # 어떠한 주소로 접근할건지 정의
    path('dinner/', views.dinner),  # views에 dinner함수
    path('hello/<str:name>/', views.hello),  # <>는 동적인 값이 들어오는 곳
    path('self_introduce/<str:name>/<int:age>/', views.self_introduce), # <><> 이렇게는 사용 불가
    path('multiply/<int:num_1>/<int:num_2>/', views.multiply),  # <>/<> 이렇게 사용해야 함
    path('dtl/', views.dtl),  # Django Template Language 연습할 페이지
    path('show_birthday/', views.show_birthday), 

]
