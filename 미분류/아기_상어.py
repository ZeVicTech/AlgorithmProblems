# https://www.acmicpc.net/problem/16236

# sort와 sorted의 차이점은 반환값에 있다.
# sort는 반환값이 none이고 sorted는 정렬된 리스트 값을 반환한다.
# bfs로 접근하는 방법은 맞았으나 구현하는데 미숙했다.
# bfs 순회하는 도중에 값을 바꾸고 위치를 변경하려고 하니까 코드가 점점 복잡해졌다.
# 하나하나 단순화시켜서 해결하는 습관을 들여야겠다.

from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

x,y = 0,0
baby_shark = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x,y = i,j

def bfs(a,b,baby_shark):
    visited = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((a,b))
    visited[a][b] = 0
    temp = []

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and graph[nx][ny] <= baby_shark:
                    q.append((nx,ny));
                    visited[nx][ny] = visited[x][y] + 1
                    if graph[nx][ny] < baby_shark and graph[nx][ny] != 0:
                        temp.append((visited[nx][ny], nx, ny))

    return sorted(temp, key = lambda x: (x[0], x[1], x[2]))

cnt = 0
check = 0
while True:
    value = bfs(x,y,baby_shark)
    if len(value) == 0:
        break
    time,nx,ny = value[0]
    graph[x][y] = 0 #물고기가 있던 자리
    graph[nx][ny] = 0 #상어가 있던 자리
    x,y = nx,ny
    cnt += time
    check += 1
    if check == baby_shark:
        check = 0
        baby_shark += 1

print(cnt)
    






