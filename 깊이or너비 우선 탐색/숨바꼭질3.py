# https://www.acmicpc.net/problem/13549

from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
visited = [-1]*100001

def bfs():
    q = deque()
    q.append(n)
    visited[n] += 1

    while q:
        value = q.popleft()

        if 0 <= value + 1 <= 100000:
            if visited[value + 1] == -1 or visited[value + 1] > visited[value] + 1:
                q.append(value + 1)
                visited[value + 1] = visited[value] + 1

        if 0 <= value - 1 <= 100000:
            if visited[value - 1] == -1 or visited[value - 1] > visited[value] + 1:
                q.append(value - 1)
                visited[value - 1] = visited[value] + 1
            

        if 0 <= 2*value <= 100000:
            if visited[2*value] == -1 or visited[2*value] > visited[value]:
                q.append(2*value)
                visited[2*value] = visited[value]

bfs()

print(visited[k])





