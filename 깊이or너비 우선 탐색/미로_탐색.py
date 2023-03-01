# https://www.acmicpc.net/problem/2178

"""
이 문제르 풀어보면서 느낀건 내가 dfs의 특성 살려서 구현하는 것을 잘 못한다는 것을 알았다.
최단거리는 bfs가 대부분 효율적이므로 웬만하면 bfs로 구현하자
"""

# 스택으로 구현한 방법(통과)
# import sys
# n,m = map(int,input().split())
# graph = [sys.stdin.readline().rstrip() for _ in range(n)]
# visited = [[-1]*m for _ in range(n)]

# def dfs():
#     dx = [1,0,-1,0]
#     dy = [0,1,0,-1]
#     stack = []
#     stack.append((0,0))

#     while stack:
#         x,y = stack.pop()
#         visited[x][y] += 1
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '1':
#                 if visited[nx][ny] == -1:
#                     stack.append((nx,ny))
#                     visited[nx][ny] = visited[x][y]
#                 else:
#                     if visited[nx][ny] > visited[x][y] + 1:
#                         stack.append((nx,ny))
#                         visited[nx][ny] = visited[x][y]


"""
재귀함수로 구현한 버전(시간초과)
"""
n,m = map(int,input().split())
graph = [sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
distance = [[int(1e9)]*m for _ in range(n)] # 최단 경로
distance[0][0] = 0
def dfs_recursive(x,y):

    if x == n-1 and y == m-1:
        return

    visited[x][y] = 1

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and graph[nx][ny] == '1':
                if distance[nx][ny] > distance[x][y] + 1:
                    distance[nx][ny] = distance[x][y] + 1
                dfs_recursive(nx,ny)

    visited[x][y] = 0

dfs_recursive(0,0)
print(distance[n-1][m-1]+1)