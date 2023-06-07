'''
작성일 : 2023년 6월 7일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 9장 함수와 모듈
'''
#알고리즘
#랜덤 블로그 선언

#함수
    #수를 전달받는다.
        #
        #


#메인
    #첫번째 수와 두 번째 수를 0부터 시작
    #5번 반복
        #함수 호출
        #반환 받은 값을 출력
        #변수에 '='을 입려받는다.
        #만약 반환 받은 값에 '='가 있다면
            #"정답입니다." 출력
            #첫 번째 수를 하나추가
        #아니면
            #"오답입니다." 출력
            #두 번쨰 수 하나추가
    #정답과 오답 값을 출력
    #만약 
        #"당신은 천재입니다." 출력

import random

#함수
def make_question() :
    num1 = random.randint(1,40)
    num2 = random.randint(1,20)
    op = random.randint(1,3)
    
    que = str(num1)
    
    if op == 1 :
        que = que + "+"
    if op == 2 :
        que = que + "-"
    if op == 3 :
        que = que + "*"
    
    que = que + str(num2)
    
    return que

#메인
R_ans = 0
W_ans = 0

for i in range(5) :
    que = make_question()
    print(que, end='')
    
    result = int(input('='))
    
    if eval(que) == result :
        print("정답입니다.")
        R_ans += 1
    else :
        print("오답입니다.")
        W_ans += 1
        
print("정답 : ", R_ans, "오답 : ", W_ans)

#if R_ans == 5 :
#    print("당신은 천재입니다.")