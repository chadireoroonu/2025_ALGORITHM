# 가장 긴 증가하는 부분 수열 3
# https://www.acmicpc.net/problem/12738
# https://chadireoroonu.tistory.com/324

import sys

def find(arr, target): # 현재 숫자가 들어갈 위치 찾기
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid
    return left

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
lis = [] # 증가하는 숫자들을 넣은 수열

for num in A: # 모든 수에 대해 들어갈 자리 찾아서 추가/교체
    idx = find(lis, num)
    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num

print(len(lis))