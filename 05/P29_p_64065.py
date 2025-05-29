# 튜플
# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    # 주어진 튜플의 맨 앞, 맨 뒤 괄호 두개씩 지우고 '},{' 기준으로 분리
    nums = list(map(str, s[2:len(s) - 2].split('},{')))
    
    # 분리한 튜플을 , 기준으로 분리, 숫자형으로 저장
    for i in range(len(nums)):
        nums[i] = list(map(int, nums[i].split(',')))
    
    # 길이가 짧은 것부터 정렬
    nums.sort(key=len)
    answer.append(nums[0][0]) # 맨 첫 숫자 저장
    
    # 인덱스 1부터 끝까지 순회하며 이미 추가되지 않은 튜플 요소 추가
    for i in range(1, len(nums)):
        for j in range(i + 1):
            if nums[i][j] not in answer:
                answer.append(nums[i][j])

    return answer
