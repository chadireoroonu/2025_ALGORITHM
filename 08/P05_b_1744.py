# 수 묶기
# https://www.acmicpc.net/problem/1744

import sys, heapq

def sol(arr, t): # t로 양수 음수 구분
    result = 0
    while len(arr) > 1:
        x = heapq.heappop(arr)
        y = heapq.heappop(arr)

        if t and y > -2: # 양수면서 y가 1 이라면
            return result - x - y - sum(arr)

        result += x * y

    return result - sum(arr) if t else result + sum(arr)

N = int(sys.stdin.readline())
plus = []
minus = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x < 1:
        heapq.heappush(minus, x)
    else:
        heapq.heappush(plus, -x) # 최대힙을 위한 음수처리

print(sol(plus, True) + sol(minus, False) if N > 1 else sum(minus) - sum(plus))