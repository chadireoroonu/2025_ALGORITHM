# 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import sys, heapq

N = int(sys.stdin.readline())
queue = []
result = 0 # 현재까지의 비교 횟수

for _ in range(N): # 입력처리
    heapq.heappush(queue, int(sys.stdin.readline()))

while len(queue) > 2:
	# 가장 작은 두 수 더하기
    x = heapq.heappop(queue)
    y = heapq.heappop(queue)
    result += x + y # 현재까지의 비교 횟수 추가
    heapq.heappush(queue, x + y) # 묶음 추가

# 주어지는 카드가 1묶음이면 비교 불필요
print(result + sum(queue) if N > 1 else 0)