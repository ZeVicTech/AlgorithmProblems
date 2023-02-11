# https://www.acmicpc.net/problem/10026

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
visited_blind = [[0] * n for _ in range(n)]

def dfs(a,b):

    color = graph[a][b]

    stack = []
    stack.append((a,b))
    visited[a][b] = 1

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while stack:
        x,y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and color == graph[nx][ny]:
                    stack.append((nx,ny))
                    visited[nx][ny] = 1

def dfs_blind(a,b):

    color = graph[a][b]

    stack = []
    stack.append((a,b))
    visited_blind[a][b] = 1

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while stack:
        x,y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if color == 'R' or color == 'G':
                    if visited_blind[nx][ny] == 0 and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G'):
                        stack.append((nx,ny))
                        visited_blind[nx][ny] = 1
                elif visited_blind[nx][ny] == 0 and color == graph[nx][ny]:
                    stack.append((nx,ny))
                    visited_blind[nx][ny] = 1


cnt = 0
cnt_blind = 0
    
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            cnt += 1

for i in range(n):
    for j in range(n):
        if visited_blind[i][j] == 0:
            dfs_blind(i,j)
            cnt_blind += 1

print(cnt, cnt_blind)



        





