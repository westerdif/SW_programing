'''
작성일 : 2023년 4월 4일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 사다리꼴의 넓이를 구한다
'''
#국어 점수를 입력 받아 변수에 저장한다.
ko = int(input('국어 점수 값을 입력하시오 :'))

#수학 점수를 입력 받아 변수에 저장한다.
math = int(input('수학 점수 값을 입력하시오 :'))

#사회 점수를 입력 받아 변수에 저장한다.
social = int(input('사회 점수 값을 입력하시오 :'))

#과학 점수를 입력 받아 변수에 저장한다.
science = int(input('과학 점수 값을 입력하시오 :'))

#역사 점수를 입력 받아 변수에 저장한다.
history = int(input('역사 점수 값을 입력하시오 :'))

#총점을 계산해 변수에 저장
total = ko + math + social + science + history

#평균을 계산해 변수에 저장
avg = total/5

#계산한 값을 출력
print("귝어: {} 수학: {} 사회: {} 과학: {} 역사: {}".format(ko,math,social,science,history))
print("총점: {}입니다    평균: {}".format(total, avg))
print("총점: {}입니다    평균: {:.2f}".format(total, avg))