# 가장 가까운 같은 글자
# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    alphabet = {} # 글자 인덱스를 저장할 딕셔너리
    
    for i in range(len(s)):
        char = s[i]
        # 현재 인덱스 - 이전 등장 인덱스
        # 처음 등장한 글자라면 -1
        d = i - alphabet[char] if char in alphabet else -1
        answer.append(d)
        alphabet[char] = i # 딕셔너리에 인덱스 추가

    return answer