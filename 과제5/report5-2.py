'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 'score.txt' 파일에 있는 4명의 학생의 국어, 수학, 영어, 성적 자료를 읽어 학생별 총점과 평균을 구하고 국어, 수학, 영어 과목의 전체 평균을
        구한 후에 화면과 'report.txt' 파일에 출력하는 프로그램
'''
#num.txt 파일을 쓰기 모드로 연다.
    #네 명의 학생 정보를 줄 단위로 리스트에 저장
    #writelines()함수를 사용해서 파일을 작성
#num.txt 파일을 읽기 모드로 연다.
    #반복문을 사용해서 파일을 반복한다.
    #각 줄을 읽어온 후, 줄바꿈 문자를 제거하고 공백으로 분리된 항목들을 변수에 저장
    #학생 이름은 첫 번째이므로, 학생 이름을 name 변수에 저장
    #나머지는 점수이므로, 점수를 정수로 변환한 후 scores 리스트에 저장
    #리스트로 학생의 총점과 평균을 계산
    #계산한 결과를 출력
#각 과목의 전체 평균을 계산해서 출력
with open('score.txt', 'w') as f:
    lines = [
        "김말동 99 83 78\n",
        "이말동 88 79 95\n",
        "정말동 77 90 81\n",
        "한말동 87 90 100\n"
    ]
    f.writelines(lines)

with open('score.txt', 'r') as f:
    kor_total = 0 #변수 초기화
    math_total = 0 #변수 초기화
    eng_total = 0 #변수 초기화
    count = 0 #변수 초기화
    for line in f:
        line = line.strip() 
        items = line.split()

        name = items[0]
        scores = [int(score) for score in items[1:]]

        kor_total += scores[0]
        math_total += scores[1]
        eng_total += scores[2]

        count += 1
        total_score = sum(scores)
        avg = total_score / len(scores)

        print("{} 총점: {} 평균: {:.2f}".format(name, total_score, avg))

    print("국어 전체 평균: {:.2f}".format(kor_total / count))
    print("수학 전체 평균: {:.2f}".format(math_total / count))
    print("영어 전체 평균: {:.2f}".format(eng_total / count))