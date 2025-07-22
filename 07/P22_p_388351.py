# 유연근무제
# https://school.programmers.co.kr/learn/courses/30/lessons/388351

def solution(schedules, timelogs, startday):
    answer = 0
    safe = [] # 지각 마지노선 시간
    for s in schedules: # 마지노선 구해서 저장
        safe.append(s // 100 * 60 + s % 100 + 10)
    
    def check(n): # 평일에 지각한 적이 있는지 확인
        for i in range(len(timelogs[n])):
            if ((i + startday) % 7) not in [0, 6]:
                hour = timelogs[n][i] // 100
                minute = timelogs[n][i] % 100
                
                # 평일에 지각하면 0 리턴 후 종료
                if hour * 60 + minute > safe[n]:
                    return 0
        return 1 # 평일에 지각하지 않아서 상 받는다
    
    # 모든 직원의 check 함수 결과 더하기
    answer = sum(check(i) for i in range(len(safe)))
                            
    return answer
