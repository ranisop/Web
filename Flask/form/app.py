# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/fake_naver')
def fake_naver():
    return render_template('fake_naver.html')

# fake google을 만들어보자.
@app.route('/fake_google')
def fake_google():
    return render_template('fake_google.html')

# 보내는
@app.route('/send')
def send():
    return render_template('send.html')

# 받는
@app.route('/recieve')
def receive():
    #request.args => # {'username':'dizyobu65', 'message':'안녕'} dict형태로 들어있음
    username = request.args.get('username')  # => dizyobu65
    message = request.args.get('message')  # => 안녕
    return render_template('recieve.html', username=username, message=message)

# lotto -> 회차 입력하는 페이지
@app.route('/check_lotto')
def check_lotto():
    return render_template('check_lotto.html')

# lotto -> 결과 확인할 수 있는 페이지
@app.route('/result_lotto')
def result_lotto():
    n = request.args.get('round_lotto') # 회차 정보 받아오기

    url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}"
    response = requests.get(url)  # 응답에 대한 모든 내용들이 담김
    lotto = response.json()  # .text라고 하면 리턴값이 string / .jason으로 하면 리턴값이 dictionary
    
    winner = []
    winner = [lotto[f'drwtNo{i}'] for i in range(1, 7)]
    bonus = lotto['bnusNo']
    
    ## 입력값
    inputs = []
    for i in range(1, 8):
        inputs.append(int(request.args.get(f'no{i}')))

    ## 비교
    matched = list(set(winner) & set(inputs))  # 중복되는 숫자들
    count = len(matched)

    if count == 6:
        reward = '1'
    elif count == 5:
        if bonus in inputs:
            reward = '2'
        else:
            reward = '3'
    elif count == 4:
        reward == '4'
    elif count == 3:
        reward == '5'
    else:
        reward == '0'

    return render_template('result_lotto.html', n=n, winner=winner, bonus=bonus, inputs=inputs, reward=reward)



if __name__ == '__main__':
    app.run(debug=True)