'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 8장 파일 입출력
'''     
print("=====학생 정보 읽어오기 1=====")
with open("student.txt", 'r') as f :
    while True:
        stu = f.readline()
        print(stu, end='')
        
        if stu == '' :
            break

print("=====학생 정보 읽어오기 2=====")
with open("student.txt", 'r') as f :
    while True:
        stu = f.readline()
        StudentList = stu.split()
        print(StudentList)
        
        if stu =='' :
            break