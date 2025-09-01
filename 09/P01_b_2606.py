# 바이러스
# https://www.acmicpc.net/problem/2606

import sys
sys.stdin = open("input.txt")

C = int(sys.stdin.readline())
M = int(sys.stdin.readline())
connected = [[] for _ in range(C + 1)]

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    connected[s].append(e)
    connected[e].append(s)

stack = [1]
visited = [0] * (C + 1)
visited[1] = 1

while stack:
    x = stack.pop()
    
    for nx in connected[x]:
        if not visited[nx]:
            stack.append(nx)
            visited[nx] = 1
    
print(sum(visited) - 1)