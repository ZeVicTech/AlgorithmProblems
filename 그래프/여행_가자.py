# https://www.acmicpc.net/problem/1976

"""
유니온 파인드를 활용해서 해결한 문제
인접 행렬로는 데이터를 받은 것은 오랜만이라 살짝 헤멨었음
인접 행렬로 구현하는 것도 가끔 시도해봐야겠다.
"""

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


n = int(input())
m = int(input())

parent = [0]*(n+1)

for i in range(n+1):
    parent[i]=i

graph = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i+1,j+1,parent)

plans = list(map(int,input().split()))

for i in range(1,n+1):
    find_parent(parent,i)

temp = []
for city in plans:
    temp.append(parent[city])

temp = set(temp)

if len(temp) == 1:
    print('YES')
else:
    print('NO')
