# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

a.sort()# 이진탐색을 하기 위해 미리 정렬 시켜둠

def binary_search(num):# 이진탐색 시행하는 함수
    start, end = 0, n-1 # 인덱스 기준

    while start<=end:
        mid = (start + end)//2
        if num > a[mid]:
            start = mid + 1
        elif num < a[mid]:
            end = mid - 1
        else:
            return 1
    return 0

for num in x:
    print(binary_search(num))


