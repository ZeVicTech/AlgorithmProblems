# https://www.acmicpc.net/problem/1927

import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(h,x)
    else:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)