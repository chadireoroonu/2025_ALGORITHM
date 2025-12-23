# 조약돌 꺼내기
# https://www.acmicpc.net/problem/13251

import sys
sys.stdin = open("input.txt")

def sol(arr, n):
    result = 0
    for i in range(len(arr)):
        temp = 1
        for j in range(n):
            temp *= (arr[i] - j) / (sum(arr) - j)
        result += temp

    return result

M = int(sys.stdin.readline())
C = int(sys.stdin.readline()) if M < 2 else list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())

print(sol(C, K) if M > 1 else 1.0)