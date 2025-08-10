# 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/problem/11054
# https://chadireoroonu.tistory.com/323

import sys
sys.stdin = open("input.txt")

def find(arr): # 증가하는 부분 수열 구하기
    dp = [1] * N
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

 # 증가하는 부분 수열
plus = find(A)

# 감소하는 부분 수열
A.reverse() 
minus = find(A)
minus.reverse()

maxi = 0
for i in range(len(A)):
    maxi = max(maxi, plus[i] + minus[i] - 1)

print(maxi)