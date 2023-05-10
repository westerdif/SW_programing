'''
작성일 : 2023년 5월 10일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 구구단의 짝수만 출력하는 프로그램으 작성하시오
문제분석:  2단부터 9단까지
           짝수만 출력
'''
#단은 2부터
dan = 2
dan_number = 2

#2부터 9단까지 반복하면서
    #곱하는 수는 1~9까지
        #실행정지
        
while dan <= 9:
    print("## {}단 ##" .format(dan_number))
    dan_number = dan_number + 1
    i = 1
    
    while i <= 9:
        if (dan * i) % 2 == 0:
            print(dan, "*", i, "=", "{}" .format(dan * i))
        i = i + 1
    dan = dan + 1
        
##### for문 ######

for dan in range(2, 10):
    print("=====", dan, "====")
    
    for i in range(1, 10):
        if dan * i % 2 ==0:
            print(dan, "*", i, "=", "{}" .format(dan * i))