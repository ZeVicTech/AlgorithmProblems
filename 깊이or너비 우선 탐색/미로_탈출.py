# https://school.programmers.co.kr/learn/courses/30/lessons/159993

"""
조건이 존재하는 전형적인 최단 거리 탐색 문제였다.
"""

from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'L':
                lever_x = i
                lever_y = j
            elif maps[i][j] == 'E':
                exit_x = i
                exit_y = j
            elif maps[i][j] == 'S':
                start_x = i
                start_y = j
    
    distance = bfs(start_x,start_y,n,m,maps)
    
    if distance[lever_x][lever_y] == -1 or distance[exit_x][exit_y] == -1:
        return -1
    
    answer += distance[lever_x][lever_y]
    
    distance = bfs(lever_x,lever_y,n,m,maps)

    answer += distance[exit_x][exit_y]
    
    
    return answer

def bfs(a,b,n,m,maps):
    visited = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((a,b))
    visited[a][b] = 0
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < m:
                if maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited
    
                    
                    
            
        
        
        
        
        
        
        
        
        
        
    
    