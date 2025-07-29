# 암호 만들기
# https://www.acmicpc.net/problem/1759

import sys

L, C = map(int, sys.stdin.readline().split())
alphabets = list(map(str, sys.stdin.readline().split()))
alphabets.sort()
vowels = {'a', 'e', 'i', 'o', 'u'}

def code(s, now, t, n):
    if len(now) == L:
        if  t and n > 1:
            return print(now)
        else:
            return
    for i in range(s, C):
        if alphabets[i] in check:
            code(i + 1, now + alphabets[i], True, n)
        else:
            if t:
                code(i + 1, now + alphabets[i], True, n + 1)
            else:
                code(i + 1, now + alphabets[i], False, n + 1)

code(0, '', False, 0)