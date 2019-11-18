from django.db import models

# Create your models here.

# M:N

# Doctor : Patient (1:N)
# 1번 : 1번
# 1번 : 2번
# 2번 : 3번
# 2번 : 1번(x)
# 적합한 구조는 아님, 어떠한 문제가 생기는지 보쟈

# 1. Doctor : Patient (1:N) -> ForeignKey 사용
# 2. Doctor : Reservation : Patient (1:N + 1:N) 
# # 의사가 여러개 진료차트 가질 수 있고, 환자도 여러개의 진료차트 가질 수 있다.
# 3. Doctor : Patient (M:N) -> ManyToManyField 사용(through를 통해 Reservation 사용)
# 4. Doctor : Patient (M:N) -> ManyToManyField 사용(Reservation 사용 안함) -> 의사, 환자 말고 별도의 데이터가 없을 경우에만 가능

class Doctor(models.Model):
    name = models.CharField(max_length=20)

class Patient(models.Model):
    name = models.CharField(max_length=20)
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # doctors = models.ManyToManyField(Doctor, through='Reservation')
    doctors = models.ManyToManyField(Doctor, related_name='patients') # doctor 쪽에서 환자를 부를 때 어떻게 부를지 related_name에 지정해주기

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
