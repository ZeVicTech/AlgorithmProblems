# https://www.youtube.com/watch?v=acqm9mM1P6o&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 1:01:20

# 플로이드 워셜 알고리즘으로 해결한 문제

n,m = map(int,input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

x,k = map(int,input().split())

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])




