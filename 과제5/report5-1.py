'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 1~100사이의 난수를 발생시켜 'num.txt' 파일을 생성하고, 생성된 'num.txt' 파일을 읽어 각 학생의 평균을 'avg.txt' 파일에 출력하는 프로그램
'''
#랜덤 블로그를 선언
#num.txt 파일을 쓰기 모드로 열고 난수를 생성하여 파일에 저장
    #5번 반복
    #5번 반복
        #1부터 100사이에서 5개의 난수를 생성해서 리스트에 저장
        #리스트의 난수를 문자열로 변화시켜서 파일에 저장
#num.txt 파일을 일기 모드로 열고 학생별 평균을 계산해서 출력
    #5번 반복
        #한 줄씩 파일을 읽어온다
        #숫자들을 리스트로 분리
        #숫자들의 합을 계산
        #평균을 계산
        #몇 번째 학생인지와 계산한 평균을 출력
import random

with open("num.txt", "w") as f:
    for _ in range(5):
        num_list = [str(random.randint(1, 100)) for _ in range(5)]
        f.write(" ".join(num_list) + "\n")

with open("num.txt", "r") as f:
    for i in range(5):
        line = f.readline()
        numbers = line.split()
        total = sum(int(num) for num in numbers)
        avg = total / len(numbers)
        print("{}번째 학생의 평균: {}".format(i + 1, avg))