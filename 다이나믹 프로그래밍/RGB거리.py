# https://www.acmicpc.net/problem/1149

"""
다른 사람의 아이디어를 참고해서 해결한 문제
처음에는 bfs, dfs를 해결하려고 했지만 경우의 수가 너무 많아 메모리 초과 또는 시간 초과가 나왔다.
문제를 접근할때 항상 입력조건을 확인하자
dp문제를 해결하는게 아직도 익숙치 않다.
큰 틀을 잡고 문제를 계속해서 작게 나눠서 점화식을 완성시켜야한다.
"""

from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

r = [0]*n
g = [0]*n
b = [0]*n

r[0],g[0],b[0]  = graph[0][0],graph[0][1],graph[0][2]

for i in range(1,n):
    r[i] = graph[i][0] + min(g[i-1],b[i-1])
    g[i] = graph[i][1] + min(r[i-1],b[i-1])
    b[i] = graph[i][2] + min(r[i-1],g[i-1])

print(min(r[n-1],g[n-1],b[n-1]))





# result = []
# def bfs():
#     q = deque()
#     q.append((0,0,0))
#     q.append((1,0,0))
#     q.append((2,0,0))

#     while q:
#         value = q.popleft()
#         if value[1] == n:
#             result.append(value[2])
#             continue

#         for i in range(3):
#             if value[0] == i:
#                 continue
#             q.append((i,value[1] + 1, value[2] + graph[value[1]][i]))

# bfs()
# print(min(result))

# result = []
# def dfs(prev,cur,value):

#     if cur == n:
#         result.append(value)
#         return
    
#     if prev != 0:
#         dfs(0,cur+1,value + graph[cur][0])
#     if prev != 1:
#         dfs(1,cur+1,value + graph[cur][1])
#     if prev != 2:
#         dfs(2,cur+1,value + graph[cur][2])

# dfs(-1,0,0)

# print(min(result))




    