# https://www.acmicpc.net/problem/17070

"""
시간초과가 나서 고생한 문제이다.
완전탐색으로 해결했지만 시간이 너무 걸려서 python3를 이용할 경우 70퍼센트에서 시간초과가 났다.
그래서 pypy3를 써서 돌려봤지만 이번엔 메모리초과가 났다.
해결방법을 찾던 도중 setrecursionlimit()를 통해 재귀깊이가 수정되면서 메모리 초과가 났던것이다.
그래서 깊이를 더 작게하거나 없앴더니 통과가 가능했다.
하지만 여전히 시간효율이 좋지않아 다른 방법이 있을까 생각했는데 dp를 활용해서 해결할 수 있다고 한다.
그래서 dp로 풀어볼 예정이다.
"""

import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

cnt = 0

def dfs(x,y,pos): # pos가 1이면 가로, 2이면 세로, 3이면 대각선
    global cnt
    if x == n-1 and y == n-1:
        cnt += 1
        return
    
    if pos == 1:
        if 0 <= x < n and 0 <= y+1 < n:
            if graph[x][y+1] == 0:
                dfs(x,y+1,1)
        if 0 <= x+1 < n and 0 <= y+1 < n:
            if graph[x+1][y+1] == 0 and graph[x][y+1] == 0 and graph[x+1][y] == 0:
                dfs(x+1, y+1, 3)

    elif pos == 2:
        if 0 <= x+1 < n and 0 <= y < n:
            if graph[x+1][y] == 0:
                dfs(x+1,y,2)
        if 0 <= x+1 < n and 0 <= y+1 < n:
            if graph[x+1][y+1] == 0 and graph[x][y+1] == 0 and graph[x+1][y] == 0:
                dfs(x+1, y+1, 3)

    elif pos == 3:
        if 0 <= x < n and 0 <= y+1 < n:
            if graph[x][y+1] == 0:
                dfs(x,y+1,1)
        if 0 <= x+1 < n and 0 <= y < n:
            if graph[x+1][y] == 0:
                dfs(x+1,y,2)
        if 0 <= x+1 < n and 0 <= y+1 < n:
            if graph[x+1][y+1] == 0 and graph[x][y+1] == 0 and graph[x+1][y] == 0:
                dfs(x+1, y+1, 3)

if graph[n-1][n-1] == 0:
    dfs(0,1,1)

print(cnt)