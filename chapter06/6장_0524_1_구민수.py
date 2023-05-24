#튜플 생성
tuple1 = ()  # 빈 튜플
tuple2 = ('a',) # 원소가 하나여도 쉼표(,)는 필수
tupel3 = ('a','b','c')

color = ('white', 'black', 'white', 'aquamarin', 'white', 'gray', 'gray')
print("color의 내용 : ", color)
print("color의 길이 : ", len(color))
print("white의 갯수 : ", color.count('white'))
print("black의 위치", color.index('black'))

#실습 예제 6-7
# 2개의 튜플을 하나의 리스트로 만들기
fruit = ('과일', '배', '딸기', '용화과', '자두')
price = (2000,4500,8000,12000,5500)

fp_list = [] # 2개의 튜플 내용이 저장 될 리스트 생성
fp_tuple = () # 2개의 튜플 내용이 저장 될 튜플 생성

for i in range(len(fruit)) :
    fp_list.append(fruit[i])
    fp_list.append(price[i])
    # fp_tuple.append(fruit[i]) #튜플은 변경이 되지 않는다.(변경이 불가)
    
print("과일 튜플 : ", fruit)
print("가격 목록 : ", price)
print("과일과 가격 리스트 : ", fp_list)