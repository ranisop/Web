'''
동행복권(https://dhlottery.co.kr/common.do?method=main)사이트에서 회차별 당첨번호 가져오기
'''


import requests

#int(input('회차를 입력하세요: '))  # input으로 받으면 문자열이기 때문에 int를 통해 숫자로 변경/ url에 넣을거라 안해도 됨
n = input('회차를 입력하세요: ')

url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'
response = requests.get(url)  # 응답에 대한 모든 내용들이 담김
lotto = response.json()  # .text라고 하면 리턴값이 string / .jason으로 하면 리턴값이 dictionary

winner = []
'''
for i in range(1, 7):
    winner.append(lotto[f'drwtNo{i}'])
'''

# list comprehension => 그냥 for문보다 속도가 더 빠르고, 파이썬 내에서 더 권장하는 방법
winner = [lotto[f'drwtNo{i}'] for i in range(1, 7)]

bonus = lotto['bnusNo']

print(f'당첨 번호는 {winner} + {bonus}입니다.')