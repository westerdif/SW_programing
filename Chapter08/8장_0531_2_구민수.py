'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 8장 파일 입출력
'''
# writelines() 메소드
list1 = ['월요일\n', '화요일\n', '수요일\n', '목요일\n', '금요일\n', '토요일\n', '일요일\n',]

#readlines() 메소드를 사용하여 무한 반복문으로 읽기
print("====for문을 이용하여 읽기====")
with open("Linetext.txt", "r") as f :
    while True:
        line = f.readlines()
        print(line, end='')
        
        if line == '' :
            break