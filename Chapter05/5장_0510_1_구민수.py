'''
작성일 : 2023년 5월 10일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 사용자로부터 정수를 입력받아 ★를 출력하시오
문제분석: 변수의 종류로는 입력값, 행 , 열(input_num, count_line, star)
          입력값 만큼 반복
          줄만큼 반복하면서 별을 출력
'''
#정수를 입력받는다.
input_num = int(input('정수를 입력하시오 : '))

#입력값 까지 반복
    #줄까지 반복하면서
        #★를 출력
for count_line in range(input_num):
    for star in range(count_line + 1):
        print("* " ,end=' ')
    print("")