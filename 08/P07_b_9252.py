# LCS 2
# https://www.acmicpc.net/problem/9252
# https://chadireoroonu.tistory.com/321

import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1): # 최장 문자열의 길이 구하기
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

i, j = len(A), len(B)
print(dp[i][j]) # 최장 문자열의 길이 출력
result = ''
while i and j:
    if A[i - 1] == B[j - 1]:
        result += A[i - 1]
        i -= 1
        j -= 1

    elif dp[i - 1][j] > dp[i][j - 1]: # 글자가 달라서 위쪽 최장 길이를 가져온 경우
        i -= 1

    elif dp[i - 1][j] <= dp[i][j - 1]: # 글자가 달라서 왼쪽 최장 길이를 가져온 경우
        j -= 1

print(result[::-1]) # 최장 문자열 출력
