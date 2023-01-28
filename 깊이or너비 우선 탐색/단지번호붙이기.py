# https://www.acmicpc.net/problem/2667

# dfs 혹은 bfs를 쓰면 쉽게 풀리는 문제였다.
# 다만 dfs로 순회하면서 한번 순회할때 방문하는 노드들의 개수를 체크하고 싶은데
# 전역 변수를 사용하지 않고 체크를 하고 싶었다. <- 이과정에서 조금 헤맸다
# 재귀의 동작방식이 머리속에서 명확하게 그려지지 않았다.



def dfs(x,y,graph,visited):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    if visited[x][y] == 1:
        return 0
    if graph[x][y] == 0:
        return 0

    result = 1
    visited[x][y] = 1

    result += dfs(x+1,y,graph,visited)
    result += dfs(x-1,y,graph,visited)
    result += dfs(x,y+1,graph,visited)
    result += dfs(x,y-1,graph,visited)

    return result


n = int(input())
graph = []
visited = []
answer = []

for _ in range(n):
    graph.append(list(map(int,input())))
    visited.append([0]*n)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 1 or graph[i][j] == 0:
            continue
        answer.append(dfs(i,j,graph,visited))

answer.sort()

print(len(answer))
for item in answer:
    print(item)



