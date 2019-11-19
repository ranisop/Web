"""myform URL Configuration

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
from django.urls import path, include
from django.shortcuts import redirect

# def root(request):
#     return redirect('articles:index')

urlpatterns = [
    path('accounts/', include('accounts.urls')),  # accounts에서의 요청은 지금 이 urls.py가 아니라 accounts 안의 urls.py로 보내라
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('', lambda r: redirect('articles:index'), name='root'),  # 메인페이지에 어떤게 올지 정의할 수 있음
]

