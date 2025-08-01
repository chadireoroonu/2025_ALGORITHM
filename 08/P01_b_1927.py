# 최소 힙
# https://www.acmicpc.net/problem/1927

import sys, heapq
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
queue = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(queue, num)
    else:
        print(heapq.heappop(queue) if queue else 0)