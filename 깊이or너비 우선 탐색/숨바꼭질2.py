# https://www.acmicpc.net/problem/12851

"""
다른 사람의 아이디어를 참고해서 해결한 문제
처음에는 최단시간은 bfs로 찾아내고 경로의 개수는 dfs로 찾아내려고 했다.
그렇게 한 결과 시간초과 또는 메모리 초과 판정을 받았다.
구글링한 결과 bfs만으로 해결할 수 있다는 것을 알게되었다.
아이디어는 기존의 bfs는 한번 방문이 되면 다시 큐에 들어가지 않는다는 것을 바꾸는데 있었다.
하지만 우리는 최단 경로의 개수를 구해야하므로 만약 걸린시간이 똑같다면 방문처리가 되어있어도
다시 큐에 집어넣어서 탐색하고 목표점에 도달하면 카운트를 해주어서 구할 수 있었다.
"""

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
visited = [-1]*100001
result = 0

def bfs(start):
    global result
    q = deque()
    q.append(start)
    visited[start] += 1

    while q:
        value = q.popleft()

        if value == m:
            result += 1
            continue

        for nx in [value+1,value-1,2*value]:
            if 0 <= nx <= 100000 and (visited[nx]==-1 or visited[nx] == visited[value] + 1): # 또 다른 최단 경로를 찾기위해 거리가 같은 경우 큐에 다시 넣어서 탐색하게 함
                q.append(nx)
                visited[nx] = visited[value] + 1
        

bfs(n)
print(visited[m])
print(result)
