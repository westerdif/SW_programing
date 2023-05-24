# 실습 예제 7-1
#앤덤으로 1~100 사이의 값을 10개 생성한 세트 2개 만들고 합집합, 교집합, 차집합으로 출력하시오
#[알고리즘]
#1. 비어있는 세트 2개 만들기
#2. 앤덤으로 2개의 세트에 각각 10개의 값을 저장.
#   랜덤, 반복하면서 10개의 값을 저장.
#   1)값 저장(추가)
#3.2개의 세트 값을 출력
#4.합집합, 교집합, 차집합 출력

import random #랜덤 함수를 사용하기 위해서는 미리 지정필수

num1 = set() #set() 함수로 비어있는 세트 생성
num2 = set()

for i in range(10) :
    num1.add(random.randint(1,100))
    num2.add(random.randint(1,100))
    
print("세트의 num1 : ", num1)
print("세트의 num2 : ", num2)
print("num1과 num2의 합집합: ", num1 | num2) # |는 합집합 연산자
print("num1과 num2의 교집합: ", num1 & num2) # &는 교집합 연산자
print("num1과 num2의 차집합: ", num1 - num2)