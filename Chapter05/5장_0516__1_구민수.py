'''
작성일 : 2023년 5월 16일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 10개의 정수를 입력받아 합을 구하는 프로그램을 작성하시오.
문제분석: count = 1  
          sum = 0
          정수를 10번 까지 반복
          조건식
          짝수번쨰 수가 양수이면 음수로, 음수이면 양수로 변환
'''
count = 1
sum = 0

#1정수를 입력받는다. 다만 10까지 반복
for i in range(1,11):
    num = int(input(str(count) + "번째 정수를 입력하시오 : "))
    

    #만약 짝수번째 수 이면
        #만약 짝수번째 수가 양수이면
            #음수로 변환
    if count % 2 == 0:
        if count > 0:
            num = num * -1    
             
        #아니면
            #음수를 양수로 변환
        else:
            num = num * -1
            
    #아니면
    
    sum = sum + num
    count = count + 1 #증감식
    
#합계를 출력
print("합계는 {}입니다.".format(sum))

print("----------------------------------")

count = 1
sum = 0
while True:
    num = int(input("{}번째 정수 입력하시오 : "))
    if count % 2 == 0 :
        num = -num
    
    sum += num
    count += 1
    
    if count > 10:
        break
print("10개 정수의 합은 : {}" .format(sum))