'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : import문과 from문 동시사용
        다만, 모듈명이 들어가면 오류발생
'''
#모듈에서 pi와 Circle_Area만 사용
from PolyArea import pi, Circle_Area

#pi 값 직접 사용
print("파이 값 : ", pi)
#print("파이 값 : ", PolyArea.pi) #모듈명을 사용하는 경으 오류 발생

print("원의 넓이와 둘레를 계산한다.")
r = float(input('반지름 : '))
# print("원의 넓이 : ", PolyArea.Circle_Area(r)) # 오류발생
print("원의 넓이 : ", Circle_Area(r))