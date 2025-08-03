# 큐 2
# https://www.acmicpc.net/problem/18258

import sys
from collections import deque
sys.stdin = open("input.txt")

queue = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    input = list(map(str, sys.stdin.readline().split()))
    x = input[0]
    if x == 'push':
        queue.append(int(input[1]))
    elif x == 'pop':
        print(queue.popleft() if queue else -1)
    elif x == 'size':
        print(len(queue))
    elif x == 'empty':
        print(0 if queue else 1)
    elif x == 'front':
        print(queue[0] if queue else -1)
    elif x =='back':
        print(queue[-1] if queue else -1)