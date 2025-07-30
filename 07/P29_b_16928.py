# 뱀과 사다리 게임
# https://www.acmicpc.net/problem/16928
# https://chadireoroonu.tistory.com/317

import sys
from collections import deque

# N, M = map(int, sys.stdin.readline().split())
# shift = {}
# count = [100] * 101

# for _ in range(N + M):
#     s, e = map(int, sys.stdin.readline().split())
#     shift[s] = e

# count[1] = 0
# queue = deque([1])

# while queue:
#     x = queue.popleft()
#     if x == 100:
#         break
    
#     for i in range(1, 7):
#         nx = x + i

#         nx = shift[nx] if nx in shift else nx
#         if nx < 101 and count[nx] > count[x] + 1:
#             count[nx] = count[x] + 1
#             queue.append(nx)

# print(count[100])

N, M = map(int, sys.stdin.readline().split())
shift = {}
count = [100] * 101

for _ in range(N + M):
    s, e = map(int, sys.stdin.readline().split())
    shift[s] = e

count[1] = 0
queue = deque([1])

while queue:
    x = queue.popleft()
    if x == 100:
        break
    
    for i in range(1, 7):
        nx = x + i

        if nx > 100:
            continue

        nx = shift.get(nx, nx)
        if nx < 101 and count[nx] > count[x] + 1:
            count[nx] = count[x] + 1
            queue.append(nx)

print(count[100])