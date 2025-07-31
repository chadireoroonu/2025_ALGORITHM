# 벼락치기
# https://www.acmicpc.net/problem/14728

import sys

N, T = map(int, sys.stdin.readline().split())
info = []
dp = [0] * (T + 1)

for i in range(N):
    info.append(list(map(int, sys.stdin.readline().split())))

for time, score in info:
    for j in range(T, time - 1, -1): # 음수 인덱스 방지하며 역순회
        dp[j] = max(dp[j], dp[j - time] + score) # 최대 점수 저장

print(dp[T])