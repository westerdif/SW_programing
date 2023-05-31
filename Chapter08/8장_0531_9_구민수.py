'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 8장 파일 입출력
'''  
#문장을 입력 받아 파일에 저장
sentence = [] #빈 리스트 생성

#enter 키를 입력 할 때까지 반복하여 문자 입력 받기
while True:
    text = input("저장할 문장 입력(종료:엔터키) : ")
    if text == '' :
        break
    
    sentence.append(text + "\n") #입력 받은 내용 리스트가 추가
    
print("입력될 리스트 : ", sentence)

#sentence.txt 파일에 내용 출력(쓰기)
with open("sentence.txt", "w") as f :
    f.writelines(sentence)
    
print("sentence.txt 파일이 생성되었습니다.")