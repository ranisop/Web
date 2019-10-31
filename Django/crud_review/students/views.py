from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    # 1. 모든 students를 DB에서 가져오기
    students = Student.objects.all()

    # 2. context에 저장
    context = {
        'students' : students,
    }

    # 3. render하면서 context 넘겨주기
    return render(request, 'students/index.html', context)


def new(request):
    if request.method == 'POST': # 'GET', 'POST'
        # student를 생성함
        # 1. POST 요청으로 넘어온 데이터 가져오기(name, age)
        name = request.POST.get('name')  # new.html에서 input의 속성 중 name의 값을 입력
        age = request.POST.get('age')

        # 2. Model 클래스 사용해서 DB에 저장
        # from .models import Student 해주기
        student = Student(name=name, age=age)
        student.save()

        # 3. 생성된 학생의 상세 정보를 보는 페이지로 이동(Detail)
        #return redirect(f'/students/{student.pk}/')  # 렌더를 하지 않기 때문에 html 파일 생성안해도 됨
        return redirect('students:detail', student.pk)
    else:
        # new page를 보여주면 됨(def new)
        return render(request, 'students/new.html')
    #return render(request, 'students/new.html')

'''
# POST 요청을 받는 친구, 생성하는 역할만 하고 보여주는건 다른 애가 함
def create(request):
    # 1. POST 요청으로 넘어온 데이터 가져오기(name, age)
    name = request.POST.get('name')  # new.html에서 input의 속성 중 name의 값을 입력
    age = request.POST.get('age')

    # 2. Model 클래스 사용해서 DB에 저장
    # from .models import Student 해주기
    student = Student(name=name, age=age)
    student.save()

    # 3. 생성된 학생의 상세 정보를 보는 페이지로 이동(Detail)
    #return redirect(f'/students/{student.pk}/')  # 렌더를 하지 않기 때문에 html 파일 생성안해도 됨
    return redirect('students:detail', student.pk)
'''

def detail(request, pk):
    # 1. pk에 해당하는 student를 DB에서 가져오기
    student = Student.objects.get(pk=pk)  # student 인스턴스 반환
    
    # 2. context에 저장
    context = {
        'student' : student,
    }

    # 3. render 하면서 context 넘겨주기
    return render(request, 'students/detail.html', context)
    

def edit(request, pk):
    # 1. pk에 해당하는 학생 DB에서 가져오기
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        # student를 수정(def update)
        # 2. POST 요청을 통해 넘어온 데이터 가져오기
        name = request.POST.get('name')
        age = request.POST.get('age')

        # 3. student 인스턴스의 정보를 변경 & DB에 반영
        student.name = name
        student.age = age
        student.save()

        # 4. student 상세 페이지로 이동해서 변경내용 확인(Detail)
        #return redirect(f'/students/{student.pk}')
        return redirect('students:detail', student.pk)
    else:
        # 수정하는 페이지를 보여줌(def edit)
        # 2. context에 저장
        context = {
            'student' : student,
        }

        # 3. render 하면서 context에 넘겨주기
        return render(request, 'students/edit.html', context)

'''
# POST 요청만 받음
def update(request, pk):
    # 1. pk에 해당하는 student를 DB에서 가져오기
    student = Student.objects.get(pk=pk)

    # 2. POST 요청을 통해 넘어온 데이터 가져오기
    name = request.POST.get('name')
    age = request.POST.get('age')

    # 3. student 인스턴스의 정보를 변경 & DB에 반영
    student.name = name
    student.age = age
    student.save()

    # 4. student 상세 페이지로 이동해서 변경내용 확인(Detail)
    #return redirect(f'/students/{student.pk}')
    return redirect('students:detail', student.pk)
'''
# POST 요청만을 받음 -> redirect()
def delete(request, pk):
    if request.method == 'POST':
        # 1. pk에 해당하는 student를 DB에서 가져오기
        student = Student.objects.get(pk=pk)
        
        # 2. student 삭제(DB에서 삭제하기)
        student.delete()

        # 3. index 페이지로 이동
        #return redirect('/students/')
        return redirect('students:index')
    
    # return 없음! 오류!