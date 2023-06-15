'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 모듈 생설
'''
#사용할 상수 변수에 저장
pi = 3.14159

#함수정의
#사각형 넓이를 계산하는 함수
def Rectangle_Area(width, height):
    return width * height

#함수정의
#삼각형의 넓이를 계산한는 함수
def Triangl_Area(base, height):
    return base*height/2

#함수정의
#원의 넓이를 계산하는 함수
def Circle_Area(r):
    return pi*r*r

#함수정의
#원의 둘레를 계산하는 함수
def Circle(r):
    return 2*pi*r
