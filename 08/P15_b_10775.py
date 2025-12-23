# 공항
# https://www.acmicpc.net/problem/10775

import sys
sys.stdin = open("input.txt")

def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, i, j):
    ri = find(parent, i)
    rj = find(parent, j)
    if ri != rj:
        parent[ri] = rj


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

parent = [i for i in range(G + 1)]
planes = 0

for _ in range(P):
    g = int(sys.stdin.readline())
    
    root = find(parent, g)
    
    if root == 0:
        break
    else:
        planes += 1 # 도킹 성공
        union(parent, root, root - 1)
        
print(planes)