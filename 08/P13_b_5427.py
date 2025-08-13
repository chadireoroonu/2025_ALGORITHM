# 불
# https://www.acmicpc.net/problem/5427

import sys
from collections import deque

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
t = int(sys.stdin.readline())
for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    building = [list(map(str, sys.stdin.readline().strip())) for _ in range(h)]
    fire = [[0] * w for _ in range(h)]
    queue = deque()
    si, sj = 0, 0

    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                queue.append((i, j))
                fire[i][j] = 1
            elif building[i][j] == '@':
                si, sj = i, j
                
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < h and 0 <= nj < w:
                if building[ni][nj] != "#" and not fire[ni][nj]:
                    fire[ni][nj] = fire[i][j] + 1
                    queue.append((ni, nj))

    queue = deque()
    visited = [[0] * w for _ in range(h)]
    visited[si][sj] = 1
    def exit(i, j):
        queue.append((si, sj))
    
        while queue:
            i, j = queue.popleft()
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < h and 0 <= nj < w:
                    if  not visited[ni][nj] and building[ni][nj] != "#":
                        if visited[i][j] + 1 < fire[ni][nj] or not fire[ni][nj]:
                            queue.append((ni, nj))
                            visited[ni][nj] = visited[i][j] + 1
                else:
                    return print(visited[i][j])

        return print("IMPOSSIBLE")

    exit(si, sj)