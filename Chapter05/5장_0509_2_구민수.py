'''
작성일 : 2023년 5월 9일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 5괌고의 성적을 입력받아 각 과목의 점수, 폄균, 총점을 출력하는 프로그램을 작성
문제분석: 입력한 점수가 0 ~ 100이 아니면 유효한 성적이 아닙니다. 출력
'''
i = 1
lo = 1
sum = 0

#5번째 과목까지 반복
    #만약 입력받은 점수가 0미만 또는 100초과이면
        #유효한 성적이 아닙니다. 출력
while i <= 5:
    input_num = int(input('{}번째 과목의 성적을 입력하시오 : ' .format(lo)))
    print("1과목의 점수는 {}점 입니다." .format(input_num))
    i = i + 1
    lo = lo + 1
    if input_num < 0 or input_num > 100:
        print("유효한 성적이 아닙니다.")
        
    #아니면
    
#총점을 계산해 저장 그리고 출력
sum = sum + input_num
print("총점 : {}점 입니다." .format(sum))

#평균을 계산해 저장 그리고 출력
avg = sum/5
print("평균 : {}점 입니다." .format(avg))

print("이용해 주셔서 감사합니다.")