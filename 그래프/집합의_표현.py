# https://www.acmicpc.net/problem/1717

"""
유니온 파인드 기본 개념 문제
구현할 수 있는지를 물어봄
"""

import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

parent = [0]*(n+1)

for i in range(n+1):
    parent[i]=i

orders = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(a,b,parent):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a

for order in orders:
    if order[0] == 0:
        union(order[1],order[2],parent)
    else:
        if find_parent(parent,order[1]) == find_parent(parent,order[2]):
            print("yes")
        else:
            print('no')
