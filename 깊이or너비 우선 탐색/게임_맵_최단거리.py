from collections import deque

def solution(maps):
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    queue.append((0,0))
    
    while queue:
        row,colum = queue.popleft()
        for x,y in dir:
            if row+x >= 0 and row+x < n and colum + y >= 0 and colum +y < m:
                if maps[row+x][colum+y] == 1:
                    queue.append((row+x, colum+y))
                    maps[row+x][colum+y] = maps[row][colum] + 1
    
    if maps[n-1][m-1] == 1:
        answer = -1
    else:
        answer = maps[n-1][m-1]
                    
    return answer