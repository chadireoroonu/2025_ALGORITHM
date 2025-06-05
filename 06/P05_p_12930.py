# 이상한 문자 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    words = s.split(' ') # 공백도 포함

    for word in words:
        for i in range(len(word)):
            # 단어별로 홀수 인덱스 소문자, 짝수 인덱스 대문자 저장
            char = word[i].lower() if i % 2 else word[i].upper()
            answer += char
        answer += ' ' # 단어 끝에 띄어쓰기 추가
        
    return answer[:-1] # 마지막 띄어쓰기 삭제