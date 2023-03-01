# https://www.acmicpc.net/problem/15656

import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
temp = []

def dfs():
    if len(temp) == m:
        print(" ".join(map(str,temp)))
        return

    for i in range(n):
        temp.append(lst[i])
        dfs()
        temp.pop()

dfs()
