# https://www.acmicpc.net/problem/1389

# 플로이드 워셜로 풀었지만 bfs, 다익스트라 등으로도 해결 가능

INF = int(1e9)

n,m = map(int,input().split())
temp = [list(map(int,input().split())) for _ in range(m)]
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j] = 0

for a,b in temp:
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

min_cnt = INF
for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        cnt += graph[i][j]
    if cnt < min_cnt:
        min_cnt = cnt
        answer = i

print(answer)




