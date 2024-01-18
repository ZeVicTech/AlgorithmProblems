# 투포인터로 풀어보기

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

a.sort()

candidate = []
cnt = 0

if len(a) > 2:
    for i in range(n):
        for j in range(i+1,n):
            candidate.append((a[i]+a[j],i,j))

    for index, item in enumerate(a):
        if (item in candidate:
            cnt += 1

print(cnt)