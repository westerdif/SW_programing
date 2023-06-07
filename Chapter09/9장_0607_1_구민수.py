'''
작성일 : 2023년 6월 7일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 9장 함수와 모듈
'''
#함수 생성 - 메인 프로그램 전에 만들기만들기
#안녕하세요 3번 출력하는 함수
def print_3_time() :
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")


print("===함수 호출 1===")

# 안녕하세요 3번 출력하는 함수 호출
print_3_time()

print("-------------------------------")

def print_n_time(value, n) :
    for i in range(n) :
        print(value)

print("===함수 호출 2===")
print_n_time('hi', 5)

print("-------------------------------")
#반지름을 입력 받아 원의 넓이를 구하시오.
#반지름을 전달받아
#원의 넓이를 계산하여 결과 값을 돌려주는 함수를 작성하시오

#알고리즘
#=함수=
    #1. 반지름을 전달받는다.(3)
        #원의 넓이를 계산한다.
        #넓이 값을 돌려준다.
#=메인=
    #반지름을 입력 받는다.(1)
    #입력 받은 반지름을 가지고 함수를 호출한다.(2)
    #원의 넓이를 출력한다.(4)
    
def circle_area(radius) :
    result = radius * radius *3.14
    return result
    #return radius * radius *3.14
    
r =int(input('숫자를 입력하시오 : '))
result = circle_area(r) #함수에거 값을 반환 받을때 저장할 변수가 필요함
print("반지름이 {}인 원의 넓이는 {}" .format(r, result))

#함수 호출하여 돌려받은 결과값을 바로 출력
print("반지름이 {}인 원의 넓이는 {}" .format(r, circle_area(r)))

#두 정수를 입력 받아 큰 수를 출력하시오.
#큰 수를 판별하여 결과를 돌려주는 함수를 작성하시오.

#알고리즘
#-함수
    #전달 받은 두 수를
        #둘 중 큰 수를 판단한다.   만약 첫번쨰 수가 두번쨰 수보다 크면
            #첫번째수를 돌려준다.
        #아니면(두번째 수가 첫 번쨰 수보다 크다 )
            #두 번째 수를 돌려준다.
#-메인
    #두 정수 입력 받기(1)
    #두 정수를 가지고 함수 호출하기(2)
    #돌려 받은 결과 출력하기(4)
    
def max_num(num1, num2) :
    if num1 > num2 :
        return num1
    else :
        return num2
    
num1 = int(input('첫 번째 수 입력 : '))
num2 = int(input('두 번째 수 입력 : '))

max_num(num1, num2)

print("두 수 중 큰 수는: ", max_num(num1, num2))