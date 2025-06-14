# 과일 장수
# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    i = 1
    while i * m <= len(score):
        answer += (score[i * m - 1] * m)
        i += 1
    
    return answer
