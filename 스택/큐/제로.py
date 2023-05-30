# https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline

k = int(input())

acc = []
for i in range(k):
    temp = int(input())
    if temp == 0:
        acc.pop()
    else:
        acc.append(temp)

print(sum(acc))