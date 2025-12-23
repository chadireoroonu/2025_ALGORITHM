# 2018 KAKAO BLIND RECRUITMENT [1차]비밀지도
# https://school.programmers.co.kr/learn/courses/30/lessons/17681
# https://chadireoroonu.tistory.com/330

def solution(n, arr1, arr2):
    answer = []
    
    def trans(m): # 10진수 -> 2진수 변환
        result = [0] * n 
        
        # 뒷자리부터 나머지 기록
        for i in range(n):
            result[- i - 1] = m % 2
            m //= 2
            
        return result
    
    
    for i in range(len(arr1)): # arr1 길이만큼 반복
    	# arr1, arr2 i 번째 수 2진수 변환 결과
        one, two = trans(arr1[i]), trans(arr2[i])
        sol = '' # 최종 결과 저장 변수
        
        # 각 자리수에 대해 벽 여부 확인, 최종 결과 기록, 추가
        for j in range(n):
            sol += '#' if one[j] or two[j] else ' '
        
        answer.append(sol)

    return answer
