'''
작성일 : 2023년 5월 3일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 
문제분석: 
'''
#정수를 입력받는다. input_num
#
#수가 1부터  num
#
#합계는 0
#
#수가 10까지 반복하면서 num
#   a.
    #만약에 수가 입력받은 수의 배수이면:
        #합계를 계산한다.
#   b-1.
#   c.
    #아니면:
#   b-2.
        #다시 처음으로 돌아간다. continue
#   e.수를 1씩 증가시킨다.       
#합계를 출력한다.

input_num = int(input('정수를 입력하시오 :'))

num = 0
sum = 0

while num <=10 :
    num = num + 1 #증감식
    if num % input_num == 0:
        sum = sum + num
    
    else:
        continue
    
print("{}의배수의 합 : {}" .format(input_num, sum))

print("=================================================")

input_num = int(input('정수를 입력하시오 :'))

num = 1
sum = 0

while num <=10 :
    if num % input_num == 0:
        sum = sum + num
        num = num + 1 #증감식
    else:
        num = num + 1 #증감식
        continue
    
print("{}의배수의 합 : {}" .format(input_num, sum))

print("=================================================")

input_num = int(input('정수를 입력하시오 :'))

sum = 0

for num in range(1,11):
    if num % input_num == 0:
        sum = sum + num
    
    else:
        continue
    
print("{}의배수의 합 : {}" .format(input_num, sum))

