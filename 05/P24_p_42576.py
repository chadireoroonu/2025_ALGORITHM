# 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
 
def solution(participant, completion):
    people = {}
    n = 0 # 해시 값의 합
    
    # people 딕셔너리에 '참가자 해시 값 : 이름' 추가
    # 추가된 해시 값의 총합 저장
    for p in participant:
        people[hash(p)] = p
        n += hash(p)
    
    # 완주한 선수들의 해시 값 뺄셈
    for c in completion:
        n -= hash(c)
    
    # 완주하지 못한 선수를 해시 값으로 찾아 출력
    return people[n]
