'''
작성일 : 2023년 4월 19일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 :  두 숫자와 연산자를 입력받아 계산 값을 출력하는 프로그램을 작성하시오.
'''
#숫자를 입력받는다
num1 = int(input('숫자를 입력하시오 : '))

#연산자응 입력받는다.
cal = input('연산자를 입력하시오')

#숫자를 입력받는다
num2 = int(input('숫자를 입력하시오 : '))

#만약 사칙연산이 + 이거나 - 이거나 * 이거나 / 이라면
#계산 값을 출력
if cal == '+' :
    print('입력하신 숫자와 연산자의 계산 값은')
    print('{}입니다.' .format(num1 / num2))

elif cal  == '-' :
    print('입력하신 숫자와 연산자의 계산 값은')
    print('{}입니다.' .format(num1 - num2))
    
elif cal == '*' :
    print('입력하신 숫자와 연산자의 계산 값은')
    print('{}입니다.' .format(num1 * num2))
    
elif cal == '/' :
    print('입력하신 숫자와 연산자의 계산 값은')
    print('{}입니다.' .format(num1 / num2))
    
#아니면
#"해당 연산자는 없습니다." 출력
else:
    print("해당 연산자는 없습니다.")