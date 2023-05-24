'''
작성일 : 2023년 5월 24일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 로또번호
'''
#1, 로또 번호 저장 할 세트 만들기
#2, 6번 반복하면서
#   1) 1~45 사이의 값을 세트 변수에 추가
#3. 로또 번호 출력
import random

lotto1 = set()
lotto2 = set()
lotto3 = set()
lotto4 = set()
lotto5 = set()
lotto6 = set()

for i in range(6) :
    lotto1.add(random.randint(1,45))
    lotto2.add(random.randint(1,45))
    lotto3.add(random.randint(1,45))
    lotto4.add(random.randint(1,45))
    lotto5.add(random.randint(1,45))
    lotto6.add(random.randint(1,45))
    
print("로또 번호 출력 : ", lotto1)
print("로또 번호 출력 : ", lotto2)
print("로또 번호 출력 : ", lotto3)
print("로또 번호 출력 : ", lotto4)
print("로또 번호 출력 : ", lotto5)
print("로또 번호 출력 : ", lotto6)

print("------------------------------------------------")

lotto3 = set()
while True:
    lotto3.add(random.randint(1,45))
    if len(lotto3) == 6:
        break
print("이번 주 로또 번호3 : ", lotto3)