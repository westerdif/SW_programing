###함수###
#함수정의#
#가장 큰 수를 구한는 함수
def max(a,b,c):
    #만약 a가 b보다 크면
    if a > b:
        #최고값에 a를 저장
        higgest = a
    
    #아니면    
    else:
        #b를 최고값에 저장
        higgest = b
    
    #만약에 c가 최고값 보다 크면  
    if higgest < c:
        #최고값에 c를 저자
        higgest = c
    
    #최고값을 반환받는다.
    return higgest

#함수정의#
#가장 작은 수를 구하는 함수
def min(a,b,c):
    #만약 a가 b보다 크면
    if a > b:
        #b를 최저갑에 저장
        rowest = b
    
    #아니면 a를 최저값에 저장
    else:
        rowest = a
    
    #만약에 c가 최저갑 보다 크면 
    if rowest > c:
        #최저값에 c를 저장
        rowest = c
    
    #최저값을 반환
    return rowest
        

#함수정의#
#모든 수의 합을 구하는 함수
def sum(a,b,c):
    #합계를 반환한다.
    return a + b + c