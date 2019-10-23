
### ★ dictionary {key : value} ###

lunch = {
    '중국집' : '양자강',
    '한식집' : '시래기'
}
#lunch = dict(중국집='양자강')
lunch['분식집'] = '김밥카페' # 값 추가
print(lunch['중국집'])  # 값 가져오기
print()

dinner = {
    '한식집': { # 키는 string, integer, float, boolean 만 올 수 있음
        '고갯마루' : '02-123-1423',
        '순남시래기' : '02-345-4567'
    }
}
print(dinner['한식집']['고갯마루'])  # 존재하지 않는 키를 부르면 에러발생
print(dinner.get('한식집').get('고갯마루'))  # 존재하지 않는 키를 부르면 None 리턴
print(dinner.get('한식집').get('양자강'))  # 명확하지 않을 경우에는 이거 사용하는게 좋음
print()

# 기본 활용
for key in lunch:
    print(key)
    print(lunch.get(key))    
print()

# key값만 가져오기
for key in lunch.keys():  # [key, key, ... ]
    print(key)
    print(lunch.get(key))    
print()

# value값만 가져오기
for value in lunch.values():  # [value, value, ... ]
    print(value)
print()

# key, value 두 개 같이 가져오기
for key, value in lunch.items():  # [(key, value), (key, value), ... ]
    print(key)
    print(value)
print()


