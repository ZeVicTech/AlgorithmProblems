# https://www.acmicpc.net/problem/2751

import sys
n = int(input())

num = [int(sys.stdin.readline().rstrip('\n')) for _ in range(n)]
num.sort()

for n in num:
    print(n)