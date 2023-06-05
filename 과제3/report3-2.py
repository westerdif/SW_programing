'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 튜플에서 중복된 숫자와 중복 횟수를 출력하고, 중복이 제거된 요소를 리스트로 출력하는 프로그램
'''
#값이 정해진 튜플을 생성
#빈 리스트를 생성
#최초의 튜플을 출력함
#튜플에 있는 값이 없을떄 까지 반복
    #i가 list1에 있다면
        #중복된 숫자와 횟수를 출력
    #아니면
        #list1에 i를 추가한다.
#중복이 제거된 리스트를 출력
tuple1 = (1,2,4,4,2,3,7,7,9,3)
list1 = []

print("====최초의 튜플====")
print(tuple1)
 
for i in tuple1 :
    if i in list1 :
        print("중복된 숫자 : {}, {}회" .format(i, tuple1.count(i)))
        
    else :
        list1.append(i)
        
print("====중복이 제거된 리스트====")
print(list1)

print("==========================================")

tuple2 = (2,2,2,4,5,4,9,5,6,8,9,2,7,2,5,9,4,5,1,1,1)
list2 = []

print("====최초의 튜플====")
print(tuple2)

counting_numbers = []

for i in tuple2 :
    if i in list2 : 
        for j in counting_numbers : 
            if j[0] == i :
                j[1] += 1
                break
            
    else :
        list2.append(i)
        counting_numbers.append([i, 1])

print("====중복된 숫자와 횟수====")
for rec in counting_numbers :
    print("중복된 숫자 : {}, {}회" .format(rec[0], rec[1]))
    
print("====중복이 제거된 리스트====")
print(list2)