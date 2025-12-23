# 단지번호붙이기
# https://www.acmicpc.net/problem/2667

import sys
sys.stdin = open("input.txt")

def DFS(x, y):
    house = 1
    stack = [(x, y)]
    ground[x][y] = 0

    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and ground[ni][nj]:
                stack.append((ni, nj))
                ground[ni][nj] = 0
                house += 1

    return house


N = int(sys.stdin.readline())
ground = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0
aparts = []

for i in range(N):
    for j in range(N):
        if ground[i][j]:
            cnt += 1
            aparts.append(DFS(i, j))

print(cnt)
aparts.sort()
print(*aparts, sep='\n')