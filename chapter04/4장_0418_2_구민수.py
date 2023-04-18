'''
작성일 : 2023년 4월 18일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 :  현재 월을 입력받아 계절을 알려주는 프로그램을 작성하시오.
'''
#현재 월을 일력받는다.
month = int(input('현재 월를 입력하시오 : '))

#만약 월이 1 ~ 12 이라면
if 1<= month <=12:
    #아니고 현재 월이 3,4,5월 이라면
    #"봄 입니다." 출력
    if month ==3 or month ==4 or month ==5:
        print("{}월은 봄 입니다." .format(month))
       
    #아니고 현재 월이 6,7,8월 이라면
    #"여름 입니다." 출력    
    elif month ==6 or month ==7 or month ==8:
        print("{}월은 여름 입니다." .format(month))
    
    #아니고 현재 월이 9,10,11월 이라면
    #"가을 입니다." 출력    
    elif month ==9 or month ==10 or month ==11:
        print("{}월은 가을 입니다." .format(month))
    
    #아니면
    #"겨울 입니다." 출력
    else:
        print("{}월은 겨울 입니다." .format(month))    

#아니면
#해당 월은 없습니다."
else:
    print("해당 월은 없습니다.")
        

