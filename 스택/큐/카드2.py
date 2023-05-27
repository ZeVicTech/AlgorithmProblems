# https://www.acmicpc.net/problem/2164

from collections import deque

n = int(input())

q = deque([i+1 for i in range(n)])

while len(q) > 1:
    q.popleft()
    temp = q.popleft()
    q.append(temp)

print(q.pop())