'''
작성일 : 2023년 4월 19일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 :  s나이와 키에 따라 입장 가능여부를 판단하는 프로그램을 작성하시오
'''
#나이를 입력받는다.
age = int(input('나이를 입력하시오 : '))

#키를 입력받는다.
hei = int(input('키를 입력하시오 : '))

#만약 나이가 8게 이상이고 키가 120cm 이상이라면
#고속 롤러코스터 입장이 가능합니다. 출력
if age >= 8 and hei >= 120:
    print("고속 롤러코스터 입장이 가능합니다.")
    
#아니고 만약에 나이가 8게 이상이고 키가 120cm 미만이라면
#저속 롤러코스터 입장이 가능합니다. 출력
elif age >= 8 and hei < 120:
    print("고속 롤러코스터 입장이 가능합니다.")
    
#아니면
#"입장할 수 없습니다." 출력
else:
    print("입장할 수 없습니다.")