'''
작성일 : 2023년 5월 30일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 8장 파일 입출력
'''
#open() 함수로 파일 쓰기 - wrtie() 메소드 사용
f = open("C:/Users/User/Documents/text.txt", "w") #파일 오픈

#파일에 쓸 내용
for i in range(1, 11) :
    f.write("{}번쟤 메세지입니다. \n" .format(i))
    
f.close() #파일 종료