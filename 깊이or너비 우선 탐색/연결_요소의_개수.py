# https://www.acmicpc.net/problem/11724

from collections import deque

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] == 1

    while queue:
        value = queue.popleft()
        for item in graph[value]:
            if visited[item] == 0:
                queue.append(item)
                visited[item] = 1
cnt = 0

for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1
    
print(cnt)






