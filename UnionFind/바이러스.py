# https://www.acmicpc.net/problem/2606

#서로소 집합(유니온 파인드) 알고리즘으로 해결한 문제
# 새로 배운 것은 경로 압축으로 find함수를 만들었을 때 유니온이 끝난 후 각 노드마다
# find() 처리를 해줘야 한다는 것을 알게됨
# 즉, 유니온함수 안에 있는 파인드 함수로는 모든 노드가 경로 압축이 되지 않음

# def find_parent(parent,node):
#     if parent[node] != node:
#         parent[node] = find_parent(parent, parent[node])
#     return parent[node]

# def union_parent(a,b,parent):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)

#     if a>b:
#         parent[a] = parent[b]
#     else:
#         parent[b] = parent[a]

# n = int(input())
# v = int(input())

# parent = []

# for i in range(n+1):
#     parent.append(i)

# for i in range(v):
#     a,b = map(int,input().split())
#     union_parent(a,b,parent)

# for i in range(1,n+1):
#     find_parent(parent,i)

# cnt = 0
# for i in range(1,n+1):
#     if parent[i] == 1:
#         cnt += 1

# print(cnt-1)


# bfs로 푸는 방법
from collections import deque

def bfs(graph,visited,start):
    if start in visited:
        return 0
    queue = deque()
    queue.append(start)
    visited.append(start)
    while queue:
        value = queue.popleft()
        for node in graph[value]:
            if node not in visited:
                queue.append(node)
                visited.append(node)
    return len(visited)

n = int(input())
v = int(input())

graph = [[] for _ in range(n+1)]
visited = []

for i in range(v):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph,visited,1)-1)








