# 둘만의 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''    
    skips = set(ord(c) for c in skip) # skip의 아스키 코드 저장
    
    for i in range(len(s)):
        char = ord(s[i])
        cnt = 0 # skip 뺀 이동 수를 셀 변수
        
        while cnt < index:
            # z 넘어갈 경우를 위한 처리
            char = (char - ord('a') + 1) % 26 + ord('a')
            if char not in skips: # skip은 이동으로 세지 않음
                cnt += 1

        answer += chr(char) # 변경 문자열 더하기
    
    return answer
