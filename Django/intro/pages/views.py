from django.shortcuts import render
import random

# Create your views here.
def index(request): # request : 웹에서 온 요청 정보(주소뿐만 아니라 복합적으로 다)가 담겨져 있다. 
    context = {
        'name' : 'dizyobu'
    }
    return render(request, 'index.html', context) # 3번째 변수 하나로 넘겨줌 {key:value}

def dinner(request):
    foods = ['초밥', '김밥', '라면', '곱창']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
    }
    return render(request, 'dinner.html', context) # request인자, 보여줄 html, context

# Variable Routing
def hello(request, name): # 두번째 파라미터 name은 urls.py에서 작성한 name이다. 같은이름 써주기!
    context = {
        'name' : name,
    }    
    return render(request, 'hello.html', context)

# 실습
# 1. 이름과 나이를 variable routing을 통해 받아서 자기소개
def self_introduce(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'self_introduce.html', context)

# 2. 숫자 2개를 variable routing을 통해 받아 곱셈 결과 보여주기
def multiply(request, num_1, num_2):
    context = {
        'num_1' : num_1,
        'num_2' : num_2,
        'result' : num_1 * num_2,
    }
    '''
    result = num_1 * num_2
    context = {
        'num_1' : num_1,
        'num_2' : num_2,
        'result' : result
    }'''
    return render(request, 'multiply.html', context)

from datetime import datetime
# The Django template language(DTL) 연습하기
def dtl(request):
    foods = ['짜장면', '냉면', '라면', '짬뽕']
    my_sentence = 'life is short, you need python'
    messages = ['apple', 'banana', 'coconut', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'foods' : foods,
        'my_sentence' : my_sentence,
        'messages' : messages,
        'datetimenow' : datetimenow,
        'empty_list' : empty_list,
    }
    return render(request, 'dtl.html', context)

# 실습★★
# It is your birthday?
# 오늘이 자신의 생일이면 '예'를, 아니면 '아니오'를 보여주는 페이지 만들기

def show_birthday(request):
    today = datetime.now()

    #if today.month == 10 and today.day == 24:
    #    result = True
    #else:
    #    result = False

    result = (today.month == 6 and today.day == 5)
    context = {
        'result' : result,
    }
    return render(request, 'show_birthday.html', context)

