# LCS
# https://www.acmicpc.net/problem/9251

import sys
sys.stdin = open("input.txt")

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(A)][len(B)])