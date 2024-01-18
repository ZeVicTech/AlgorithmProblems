# https://www.acmicpc.net/problem/1012

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
graph = []
visited = []

def bfs(a,b,n,m):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m \
                and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                q.append((nx,ny))
                visited[nx][ny] = 1

for i in range(t): #테스트 케이스만큼 반복
    m,n,k = map(int,input().split())
    graph = [[0] * m for _ in range(n)] #테스트 케이스마다 초기화
    visited = [[0] * m for _ in range(n)]

    for j in range(k):
        a,b = map(int,input().rstrip().split())
        graph[b][a] = 1 #배추 위치 설정

    cnt = 0 #배추 흰지렁이 수(해당위치에서 bfs로 찾을 수 있는 연결그래프 수)

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1 and visited[a][b] == 0:
                bfs(a,b,n,m)
                cnt+=1

    print(cnt)
