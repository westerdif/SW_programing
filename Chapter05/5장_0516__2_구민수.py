'''
작성일 : 2023년 5월 16일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 사용자로부터 가장 좋아하는 눨을 입력 받아 그 월에 해당되는 계절을 출력하는 프로그램을 while문을 사용해서 작성하시오.
문제분석:  3,4,5월 이면 봄
           6,7,8월 이면 여름
           9,10,11월 이면 가을
           12,1,2,월 이면 겨울
           입력받은 수가 0이면 BREAK
'''
while True:
    month = int(input("가장 좋아하는 계절을 입력하시오 : "))
    if month == 0:
        break
        
    
    if 3 <= month <= 5:
        print("*****", month, "월은 *****")
        print("{}월은 봄입니다." .format(month))
        
    elif 6 <= month <=8:
        print("*****", month, "월은 *****")
        print("{}월은 여름입니다." .format(month))
        
    elif 9 <= month <= 11:
        print("*****", month, "월은 *****")
        print("{}월은 가을입니다." .format(month))
        
    elif 12 == month or 1 == month or 2 == month:
            print("*****", month, "월은 *****")
            print("{}월은 겨울입니다." .format(month))
        
    else:
        print("*****", month, "월은 *****")
        print("{}월은 존재하지 않는 월입니다." .format(month))