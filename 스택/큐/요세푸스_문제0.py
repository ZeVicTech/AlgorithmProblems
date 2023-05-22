# https://www.acmicpc.net/problem/11866

# 지금은 일반 큐로 해결했음
# idx를 계산해서 우선순위큐로 해결이 가능하다.(나중에 풀어 볼 것)

from collections import deque

n,k = map(int,input().split())

human = [i+1 for i in range(n)]

q = deque(human)

result = []

cnt = 1
while q:
    if cnt%k == 0:
        result.append(q.popleft())
    else:
        temp = q.popleft()
        q.append(temp)
    cnt += 1

print("<", end='')
for i in range(len(result)):
    if i == len(result) - 1:
        print(str(result[i]) +">")
    else:
        print(str(result[i]), end=', ')