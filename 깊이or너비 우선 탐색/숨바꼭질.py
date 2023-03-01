# https://www.acmicpc.net/problem/1697

# 알고리즘 분류를 보고 힌트를 얻어 푼 문제
# bfs 또는 dfs의 노드를 너무 한정지어 생각한다는 문제점이 있다.
# 그래프 개념을 좀 더 유연하게 적용시킬 수 있어야 할 것 같다.

from collections import deque

n,m = map(int,input().split())

visited = [-1]*100001

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = visited[start] + 1

    while q:
        value = q.popleft()

        if value - 1 >= 0 and visited[value-1] == -1:
            q.append(value-1)
            visited[value-1] = visited[value] + 1
        if value + 1 <= 100000 and visited[value + 1] == -1:
            q.append(value+1)
            visited[value+1] = visited[value] + 1
        if 2*value <= 100000 and visited[2*value] == -1:
            q.append(2*value)
            visited[2*value] = visited[value] + 1

bfs(n)
print(visited[m])


