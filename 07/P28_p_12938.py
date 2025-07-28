# 최고의 집합
# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    answer = []
    
    if s < n:
        return [-1]
    
    for i in range(n - 1):
        temp = s // (n - i)
        answer.append(temp)
        s -= temp
    
    answer.append(s)
    answer.sort()
    
    return answer