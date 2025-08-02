import sys
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
nums = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

for t in targets:
    print(1 if t in nums else 0)