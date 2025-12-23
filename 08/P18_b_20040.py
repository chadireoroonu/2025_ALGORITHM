# 사이클 게임
# https://www.acmicpc.net/problem/20040
# https://chadireoroonu.tistory.com/327

import sys
sys.stdin = open("input.txt")

def find(parent, i): # 루트 찾기
    if i == parent[i]:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, i, j): # 합치기
    if i > j: # 더 작은 숫자의 루트에 추가
        i, j = j, i
    parent[j] = i

def sol():
    n, m = map(int, sys.stdin.readline().split())
    parent = [i for i in range(n)]

    for i in range(m):
        # 두 점의 루트 찾기
        s, e = map(int, sys.stdin.readline().split())
        rs, re = find(parent, s), find(parent, e)

        if rs == re: # 루트가 같다면 사이클 발견
            return i + 1
        else: # 루트가 다르면 합치기
            union(parent, rs, re)
    return 0

print(sol())