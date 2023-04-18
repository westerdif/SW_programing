'''
작성일 : 2023년 4월 18일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 :  한 과목의 점수 구간에 따라 학점을 부여하는 프로그램을 작성하시오
'''
#점수를 변수에 저장한다.
score = int(input('점수를 입력하시오 : '))

#만약 점수가 0 ~ 100 사이이면
if score >= 0 and score <=100:
    # 점수가 90점 이상이면
    #"A학점 입니다" 출력
    if score >= 90:
        print("A학점 입니다.")
    
    # 점수가 80점 이상이면
    #"B학점 입니다" 출력
    elif score >=80:
        print("B학점 입니다.")
    
    # 점수가 70점 이상이면
    #"C학점 입니다" 출력    
    elif score >=70:
        print("C학점 입니다.")
    
    # 점수가 60점 이상이면
    #"D학점 입니다" 출력    
    elif score >=60:
        print("D학점 입니다.")
    
    #아니면 "F학점 입니다." 출력   
    else:
        print("F학점 입니다.")
#아니면 "잘 못 입력된 점수" 출력
else:
    print("잘 못 입력된 점수입니다.")