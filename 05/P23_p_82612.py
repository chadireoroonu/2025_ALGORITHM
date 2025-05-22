# 부족한 금액 계산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    total = 0
    
    # 놀이기구 총 이용료 구하기
    for i in range(count):
        total += price * (i + 1)
    
    # 부족한 금액 구하기
    answer = total - money
    
    # 금액이 충분하다면 0 리턴
    return answer if answer > 0 else 0
