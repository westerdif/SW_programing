'''
작성일 : 2023년 3월 28일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 변수 사용법과 자료형 알아보기
         print()함수 사용법 익히기.
'''
# 변수 num1dp 1을 배정하시오.
num1 = 10

# 변수 num2에 20을 배정하시오
num2 = 20 # 첫 칸에 뛰어쓰기 하지 말 것 !!

#변수에 3.14를 정자하시오
pi = 3.14

# 변수에 자기 이름을 저장하시오
name = "구민수"

# num1, num2에 저장된 값을 저하여 tatal에 저장하시오
total = num1 + num2

#각 변수에 저장된 값을 출력한다.
print("num1 변수에 저장된 값 :", num1)
print("num2 변수에 저장된 값 :", num2)

print("pi에 저장된 값은 {}입니다." .format(pi))# .format(변수 이름)

#나의 이름은 구민수입니다.
print("나의 이름은 {}입니다." .format(name))
print("나의 이름은", name, "입니다.")

# 10 + 20 = 30
print(num1, '+', num2, '=', total)
print("{} + {} = {}" .format(num1,num2,total))

# 변수의 자료형을 알아보기 위해서 사요하는 함수
# type()
print("num1의 자료형 :", type(num1))
print("pi의 자료형 :", type(pi))
print("name의 자료형 :", type(name))