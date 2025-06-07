# 푸드 파이트 대회
# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            answer += str(i)
    
    answer += '0'
   
    for i in range(len(answer) - 2, -1, -1):
        answer += answer[i]
    
    return answer