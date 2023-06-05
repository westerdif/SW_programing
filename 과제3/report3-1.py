'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 1부터 1000 사이의 소수를 구하여 리스트에 저장한 후에, 소수와 소수의 개수를 출력하는 프로그램
'''
list = []
num = 0

for i in range(2,1001) :
    for num in range(2, i+1) :
        if i % num == 0 :
            break
    
    if num == i :
        list.append(i)

print(list)
print("1부터 1000사이의 소수의 갯수는")
print("======{}개 입니다.======" .format(len(list)))