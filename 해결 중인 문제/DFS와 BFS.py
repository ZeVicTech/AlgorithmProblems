# https://www.acmicpc.net/problem/1260

from collections import deque

def bfs(visited, graph, start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        cur = queue.popleft()
        print(cur, end = ' ')
        for item in graph[cur]:
            if visited[item] == 0:
                queue.append(item)
                visited[item] = 1
    print()
    return 

def dfs(visited, graph, start):
    visited[start] = 1
    print(start)
    for item in graph[start]:
        if visited[item] == 0:
            visited[item] = 1
            dfs(visited,graph,item)



n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(m):
    graph[i].sort()

bfs(visited[:], graph, v)
dfs(visited[:], graph, v)