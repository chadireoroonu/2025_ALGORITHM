# 대충 만든 자판
# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []
    
    # 각 글자를 입력하는 최소 타이핑 횟수 찾기
    keys = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] in keys and keys[key[i]] <= i:
                    continue
            keys[key[i]] = i + 1

    # 타겟을 만드는 최소 타이핑 횟수 더하기
    for target in targets:
        count = 0
        for i in target:
            # 글자를 입력할 수 없는 경우
            if i not in keys:
                count = -1
                break        
            count += keys[i]
        answer.append(count)
            
    return answer
