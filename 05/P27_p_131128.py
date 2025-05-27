# 숫자 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    answer = ''
    
    # 입력 문자열에서 각 숫자가 몇 번 등장했는지 카운트
    def count(s):
        arr = [0] * 10
        for i in range(len(s)):
            arr[int(s[i])] += 1
            
        return arr # 배열로 반환
    
    x = count(X)
    y = count(Y)
    
    # 큰 숫자부터 공통 숫자를 찾아 answer 추가
    for i in range(9, -1, -1):
        if x[i] and y[i]:
            # 겹치는 개수를 세기 위해 min 사용
            for j in range(min(x[i], y[i])):
                answer += str(i)
    
    # 예외처리
    if not answer: # 겹치는 숫자가 없을 때
        answer = '-1'
    elif answer[0] == '0': # 겹치는 숫자가 0 뿐일 떄
        answer = '0'
    
    return answer