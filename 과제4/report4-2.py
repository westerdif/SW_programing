'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 1부터 100사이의 정수 난수를 10개를 발생시켜 리스트에 저장하고, 각 숫자의 자리수를 키 값으로 하는 딕셔너리를 생성하는 프로그램
'''
#랜덤 블로그를 선언
#난수 리스트를 저장하기 위한 빈 리스트 생성
#1부터 100사이에서 난수 10개를 발생시키기 위해 10번 반복
    #난수 리스트에 랜덤으로 10개의 난수를 저장
#생성된 난수 리스트 출력
#사용할 4개의 리스트 생성
#난수 리스트에 저장되 값이 없을때 까지 반복
    #i에 저장된 값이 없을때 까지 반복
        #만약 딕셔너리에 값이 키에 해당하는 값이 없을경우
            #새로운 키를 딕셔너리에 추가
        #키에 해당하는 값들에 현재 숫자 추가
        #만약 자리수가 1일 경우
            #1 자리수에 해당하는 숫자(num)를 num1 리스트에 추가
        #아니고 만약에 자리수가 2일 경우
            #2 자리수에 해당하는 숫자(num)를 num2 리스트에 추가
        #아니고 만약에 자리수가 3일 경우
            #3 자리수에 해당하는 숫자(num)를 num3 리스트에 추가
#딕셔너리와 리스트를 출력
import random

numbers = []
for o in range(10):
    numbers.append(random.randint(1, 100))
print("생성된 난수 리스트:", numbers)

dict1 = {}
num1 = []
num2 = []
num3 = []

for i in numbers:
    for j in str(i):
        if j not in dict1:
            dict1[j] = []
        dict1[j].append(i)
        if int(j) == 1:
            num1.append(i)
        elif int(j) == 2:
            num2.append(i)
        elif int(j) == 3:
            num3.append(i)


print("생성된 딕셔너리:", dict1)
print("1:", num1)
print("2:", num2)
print("3:", num3)