# 수들의 합 5
# https://www.acmicpc.net/problem/2018
# https://chadireoroonu.tistory.com/329

import sys
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
cnt = 0

f, r, result = 1, 1, 1
while r <= N:
    if result < N:
        r += 1
        result += r
    elif result > N:
        result -= f
        f += 1
    else:
        cnt += 1
        result -= f
        f += 1

print(cnt)