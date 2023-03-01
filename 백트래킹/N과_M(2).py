# https://www.acmicpc.net/problem/15650

"""
백트래킹을 활용한 문제이다.
N과 M(1)문제와 달리 파라미터(인자)값을 활용해야했다.
재귀를 활용하는게 아직도 익숙치가 않다.
활용하는데 시간이 오래 걸리는 편인 것 같다.
"""

n,m = map(int,input().split())
visited = [0]*(n+1)
temp = []

def dfs(start):
    if len(temp) == m:
        print(" ".join(map(str,temp)))
        return
    
    for i in range(start+1,n+1):
        if visited[i] == 0:
            temp.append(i)
            visited[i] = 1
            dfs(i)
            temp.pop()
            visited[i] = 0

dfs(0)
