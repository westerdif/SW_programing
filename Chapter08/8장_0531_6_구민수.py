'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 8장 파일 입출력
        -실습 예제
        학생 성적 저장 파일 만들기 
        wrtie() 메소드와 readlines() 메소드를 이용하여
        학생 이름과 3과목의 성적을 리스트로 생성하여 파일에 저장
        예) 홍길동 100 95 77
'''
with open("student.txt", "w") as f :
    for i in range(5) :
        student = input(str(i+1) + "번째 학생 이름과 성적 입력 :")
        f.write(student + "\n")
        

    