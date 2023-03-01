# https://www.acmicpc.net/problem/15649

"""
dfs를 활용한 백트래킹 문제
"""

n,m = map(int,input().split())
visited = [0]*(n+1)
temp = []

def dfs():
    if len(temp) == m:
        print(" ".join(map(str,temp)))
        return
    
    for i in range(1,n+1):
        if visited[i] == 0:
            temp.append(i)
            visited[i] = 1
            dfs()
            temp.pop()
            visited[i] = 0

dfs()