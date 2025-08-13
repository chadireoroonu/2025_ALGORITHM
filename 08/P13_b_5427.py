# 불
# https://www.acmicpc.net/problem/5427
# https://chadireoroonu.tistory.com/326

import sys
from collections import deque

def sol():
    # 입력처리
    w, h = map(int, sys.stdin.readline().split())
    building = [list(map(str, sys.stdin.readline().strip())) for _ in range(h)]
    fire = [[0] * w for _ in range(h)] # 불 붙는 시간
    fire_q = deque()
    si, sj = 0, 0 # 시작 위치

    # 불, 시작 위치 확인
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                fire_q.append((i, j))
                fire[i][j] = 1
            elif building[i][j] == '@':
                si, sj = i, j

    # 불 BFS 
    while fire_q:
        i, j = fire_q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < h and 0 <= nj < w:
                # 벽이 아니고 아직 불이 옮겨붙지 않은 칸에 불 옮기기
                if building[ni][nj] != "#" and not fire[ni][nj]:
                    fire[ni][nj] = fire[i][j] + 1
                    fire_q.append((ni, nj))

    exit_q = deque([(si, sj)])
    visited = [[0] * w for _ in range(h)]
    visited[si][sj] = 1

    # 탈출 BFS
    while exit_q:
        i, j = exit_q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < h and 0 <= nj < w:
                # 아직 방문하지 않았고 벽이 아닌 위치이며, 불보다 빨리 갈 수 있는 칸으로 이동
                if not visited[ni][nj] and building[ni][nj] != "#":
                    if visited[i][j] + 1 < fire[ni][nj] or not fire[ni][nj]:
                        exit_q.append((ni, nj))
                        visited[ni][nj] = visited[i][j] + 1
            else: # 건물 범위를 벗어나서 탈출 성공
                return visited[i][j]

    return "IMPOSSIBLE"

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
t = int(sys.stdin.readline())
for _ in range(t):
    print(sol())