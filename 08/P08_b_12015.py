# 가장 긴 증가하는 부분 수열 2
# https://www.acmicpc.net/problem/12015
# https://chadireoroonu.tistory.com/322

import sys
sys.stdin = open("input.txt")

def find(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
lis = []

for num in nums:
    idx = find(lis, num)

    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num

print(len(lis))