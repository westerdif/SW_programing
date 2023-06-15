'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 모듈의 계산값을 출력
'''
#모듈 선언
import PolyArea

#사각형의 가로와 세로를 입력받아 넓이를 계산
print("사각형의 넓이를 계산합니다.")
width = float(input('사각형의  가로 : '))
height = float(input('사각형의 세로 : '))
print("사각형의 넓이 : ", PolyArea.Rectangle_Area(width,height))

#삼각형의 밑변과 높이를 입력받아 넓이를 계신한다.
print("삼각형의 넓이를 계산합니다.")
base = float(input("삼각형의 밑변 : "))
t_height = float(input('삼각형의 높이'))
print("삼각형의 넓이 : ", PolyArea.Triangl_Area(base, t_height))

#원의 반지름을 입력받아 넓이와 둘레를 계산한다.
print("원의 넓이와 둘레를 계산한다.")
r = float(input('반지름 : '))
print("원의 넓이 : ", PolyArea.Circle_Area(r))
print("원의 둘레 : ", PolyArea.Circle(r))

print("파이 값 : ", PolyArea.pi)