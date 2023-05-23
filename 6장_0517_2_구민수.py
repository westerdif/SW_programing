'''
작성일 : 2023년 5월 17일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 6장 시퀀스 자료형
02. 문자열
'''
#1.문자열 생성
name = '구민수'
name2 = '''
구
민
수
'''
print("name : ", name) 
print("name2 : ", name2)

#빈 문자열 생성
text1 = ''
print("text1의 길이: ", len(text1))
text2 = str()
print("text2의 길이 : ", len(text2))

text3 = str(1234)
print("text3 : ", text3)
print("text3릐 자료형 : ", type(text3))

#리스트를 문자열로 생성.
text4 = str([1,2,3])
print("text4의 자료형 : ", type(text4)) 
#리스트 자체를 문자열로 인식 하여 '[' 출력됨
print("text4의 0번지 값 : ", text4[2]) 


#2. 문자열 메소드
#대소문자 변환
text1 = 'i like python'
print("text1 내용의 첫 문자를 대문자로 변환 : ", text1.capitalize())
print("text1 내용의 모든 단어의 첫 문자를 대문자로 변환 : ", text1.title())
text2 = text1.upper() #대문자 변환
print("text1의 내용 모든 단어를 대문자로 변환 : ", text2)
text3 = text2.lower() #소문자로 변환
print("text2의 내용 모든 단어를 소문잘 뱐환 :", text3)

#문자열 정렬
print(text3.center(30, '*'))

#문자 찾기
print("text3에 'a'가 몇개 있나요?", text3.count('a'))
print("text3에 'a'가 몇개 있나요?", text3.count('i'))
print("text3의 5부터 1-까지 중에서 'i'가 몇 개 있나요?", text3.count('i',))
print("text3의 5이후에 '0'가 몇 개 있나요?", text3.count('0',5))

#문자열 내의 위치 - index(), find(), startswitch(), endswitch()
print("text3의 'k'의 인덱스 위치는?", text3.index('k'))
print("text3의 'k'의 인덱스 위치는?", text3.find('k'))

print("text3의 'python'의 인덱스 위치는?", text3.index('python'))
print("text3의 'python'의 인덱스 위치는?", text3.find('python'))

#없으면 오류
#print("text3의 'python1'의 인덱스 위치는?", text3.index('python1'))
#없으면 -1을 반환
print("text3의 'python1'의 인덱스 위치는?", text3.find('python1'))

print("text3가 'i like'로 시작하는가?", text3.startswith('i like'))
print("text3이'abc'로 끝나는가?", text3.endswith('abc'))

#문자열 결합 -join()
#리스트 생성
list1 = ['1','2','3','4','5']
print("list1 내용에 '-'를 결합 : ", '-'.join(list1))

list2 = [1,2,3,4,5]
#오류 발생. 정수와 문자는 연결이 안됨. join()의 대상은 반드시 문자열이어야 함
#print("list2 내용에 '-'를 결합 : ", '-'.join(list2))

#딕셔너리 - 키:값(key:value)
dict1 = {'apple':'사과', 'grape':'포도', 'peach':'복숭아'}
#키(key)에 해당하는 문자열 조인
print("dict1 내용에 '-'를 결합 : ", '-'.join(dict1))

#문자열 분리 - split()
text1 = "I Like Python Language"
#문자열을 스페이스로 분리하여 리스트로 반환
list1 = text1.split() 
print("text1의 내용을 스페이스로 분리하여 리스트로 생성 : ", list1)

text2 = "I-Like-Python-Language"
print("text2의 내용을 '-'를 기준으로 분리하여 리스트로 생성 : ", text2.split('-')) #변수에 저장하는 것이 아닌 바로 반환

#문자열에서 특정 문자를 제거, 변환
text3 = "            I Like Python Language          "
print("text3의 내용 : ", text3)
print("text3 내용중 양 옆의 빈칸 제거 : ", text3.strip())

print("text1 내용 중 'Like'를 'Love'로 교체 : ", text1.replace('Like', 'Love'))

#문자열 검사
print("text1의 모든 단어의 첫 문자가 대문인가? : ", text1.istitle())

text4 = 'abc123'
print("text4의 문자열이 문자와 숫자로 구성되어 있는가?", text4.isalnum())

text5 = '1234567890'
print("text5의 문자열이 모두 숫자로 되어있는가?", text5.isdigit())
print("text5의 문자열이 모두 문자자로 되어있는가?", text5.isalpha())

print("text1의 문자열이 모두 대문자로 구성되어 있는가?", text5.isupper())
print("text1의 문자열이 모두 소문자로 구성되어 있는가?", text5.islower())
