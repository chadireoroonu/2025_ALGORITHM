# 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys
sys.stdin = open("input.txt")

def DFS(x, y):
    stack = [(x, y)]
    world[x][y] = 0
    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and world[ni][nj]:
                stack.append((ni, nj))
                world[ni][nj] = 0
    return

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    world = [[0] * M for _ in range(N)]
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
    cnt = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        world[y][x] = 1

    for i in range(N):
        for j in range(M):
            if world[i][j]:
                cnt += 1
                DFS(i, j)

    print(cnt)