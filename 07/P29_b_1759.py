# 암호 만들기
# https://www.acmicpc.net/problem/1759

import sys

L, C = map(int, sys.stdin.readline().split())
alphabets = list(map(str, sys.stdin.readline().split()))
alphabets.sort()
vowels = {'a', 'e', 'i', 'o', 'u'}

def code(s, now):
    if len(now) == L:
        vcnt = ccnt = 0
        for c in now:
            if c in vowels:
                vcnt += 1
            else:
                ccnt += 1
        if vcnt > 0 and ccnt > 1:
            print(now)

    for i in range(s, C):
        code(i + 1, now + alphabets[i])

code(0, '')