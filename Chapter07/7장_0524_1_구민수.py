'''
작성일 : 2023년 5월 24일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 7장 세트와 딕셔너리
       01. 세트
       
순서가 없으면서 중복을 허용하지 않는 자료구조
'''
set1 = {'one', 'two', 'three'}
print("세트 set1의 내용 : ", set1)

set2 = {1,2,3,4,5,4,3,2,1}
print("세트 set2의 내용 : ", set2)

set3 = {1,2,3,(1,2,3,),4}
print("세트 set3의 내용 : ", set3)

set4 = {1,2,3,(1,2,3,),4,(2,2,2)}
print("세트 set4의내용 : ", set4)

#set5 = {1,2,3[1,2,3],4}
#print("세트 set5의내용 : ", set5) # 리스트는 세트에 포함할 수 없다.
#따라서, 문자열, 튜플을 세트 자료형으로 사용 가능하지만 리스트는 적용되지 않는다.

#세트에 관힌 메소드
# add(), remove(), discard(), pop(), copy(), clear()

#추가
set6 = {1,2,3,4,5}
set6.add(6)
print("세트 set6의내용(추가) : ", set6)

#set6에 1부터 10까지 내용을 추가하시오
for i in range(1, 11) :
    set6.add(i)
    
print("세트 set6의내용(1~10 추가) : ", set6)

#삭제 remove(), discard(), pop()
set6.discard(1) # 내용 중에 1을 삭제
set6.remove(3) # 내용 중에 3을 삭제
print("세트 set6의내용(1과 3을 삭제)) : ", set6)

#set6.discard(11) # 내용 중에 11을 삭제(내용 중 없는 내용을 삭제시 오류가 발생하지 않음)
#set6.remove(11) # 내용 중에 11을 삭제(내용 중 없는 내용을 삭제시 오류발생)

set6.pop() # 첫 번째 요소가 삭제된다.(어떠한 요소도 넣지 않는다,)
print("세트 set6의내용 : ", set6)

#복사
set7 = {11,22,33,44,55}
set8 = set7.copy()
print("세트 set7의내용 : ", set7)
print("세트 set8의내용 : ", set8)

#지우기(모두 삭제)
set7.clear()
print("세트 set7의내용 : ", set7)
print("세트 set8의내용 : ", set8)

#세트 연산 메소드
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print("세트 set1의내용 : ", set1)
print("세트 set2의내용 : ", set2)
print("set1과 set2의 합집합: ", set1 | set2) # |는 합집합 연산자
print("set1과 set2의 교집합: ", set1 & set2) # &는 교집합 연산자
print("set1과 set2의 차집합: ", set1 - set2)