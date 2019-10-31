from django.db import models

# 파이썬 코드라서 데이터베이스가 알아듣지를 못해
# 그래서 알아들을 수 있게 변환해주는거 -> makemigration -> 0001_initial.py 생성
# 데이터베이스 들어가기 직전 파일

# Create your models here.
class Student(models.Model):  # Student에 대한 설계도, class 이름은 대문자로 시작하기
    #id = models.AutoField(primary_key=True)  # id값 따로 설정 안해줘도 괜찮음
    name = models.CharField(max_length=10)
    age = models.IntegerField()  # 숫자만 기록
    created_at = models.DateTimeField(auto_now_add=True)  # 새로운 데이터가 생성될때만 기록
    updated_at = models.DateTimeField(auto_now=True)  # 생성 혹은 수정 등 변경될때 기록
    
    # 1. DB에 테이블을 생성하기 위한 설계도 생성 
    # python manage.py makemigrations
    # 에러가 나면 저장이 잘 되어있는지, settings.py에 INSTALLED_APPS에 추가가 잘 되어는지 확인
    #
    # 2. 위의 설계도를 가지고 실제 DB에 테이블을 생성
    # python manage.py migrate 




# Articles
#
# id, created_at은 데이타베이스에 저장이 되어야 생기는 것

# 
# 1. models.py에 원하는 class 작성
# 2. python manage.py makemigrations
#    -> medels.py를 바탕으로 설계도(migration 파일) 생성
# 3. python manage.py migrate
#    -> DB(db, sqlite3)에 설계도를 적용(테이블 생성)
#


# DB에 데이터를 생성하는 방법 3가지
# 1. article = Article()
#    article.title = '제목'
#    article.content = '내용'
#    article.save()
#
# 2. article = Article(title='두번째', content='두번째 내용')
#    article.save()
#
# 3. article = Article.objects.create(title='세번째', content='세번째 내용')


# Read
# 1. All - Article.objects.all()  # 복수(QuerySet), 데이터베이스 모두 불러올 수 있음
#
# 2. 1개 - Article.objects.get(id=1)  # 단수(인스턴스), get은 무조건 하나만 나옴, 조건을 주고 검색
#          Article.objects.get(title='세번째')  # title 같은게 여러개이면 에러발생
#          # unique한 컬럼으로 가져오는게 좋음! => id!! get은 id랑 쓰기
#          # 결과가 0이어도 에러 발생, 오직 1개만 가능
#
# 3. 조건 - Article.objects.filter(title='세번째')  # 복수가능, where랑 비슷
#
# 4. QuerySet + .first(), last()  # 단수
#    Article.objects.filter(title='세번째').first()  # 조건이 맞는 결과값 중에서 첫번째꺼 출력
#    Article.objects.filter(title='세번째').last()  # 조건이 맞는 결과값 중에서 마지막꺼 출력
#
# 4-1. Article.objects.filter(title='안녕')                                   
#      Out[16]: <QuerySet []>  # 조건에 맞는 결과가 없을 때 filter는 에러가 아니라 빈값을 출력
# 4-2. order_by(컬럼명)
#      Article.objects.all().order_by('title')  # title 기준으로 오름차순 정렬
#      Article.objects.all().order_by('-title')  # - 붙이면 내림차순 정렬
# 4-3. offset, limit (OFFSET, LIMIT) [offset:offset+limit]
#      Article.objects.all()[1:3]  # => [2,3]


# Update
# 1. 데이터 가져오기 
#    a = Article.objects.get(id=1)  
#    a.title  # '첫번째 글 입니다.'
# 2. 수정할 값 할당하기 
#    a.title = 'First!' 
#    a.title  # 'First!'
# 3. 저장하기(DB에 반영)
#    a.save()


# Delete    
# 1. 데이터 가져오기
#    a = Article.objects.get(id=1)
#    a  # <Article: 1번 글 - First! : 내용입니다.>
# 2. 데이터 삭제하기(DB에 반영)
#    a.delete()
#    a  # <Article: None번 글 - First! : 내용입니다.> # 호출하면 id 없음
#    Article.objects.all()  # DB 불러보면 id=1 없음                                          
#    # => <QuerySet [<Article: 2번 글 - 두번째 : 두번째 내용>, <Article: 3번 글 - 세번째 : 세번째 내용>, <Article: 4번 글 - 세번째 : 세번째 내용2>]>
