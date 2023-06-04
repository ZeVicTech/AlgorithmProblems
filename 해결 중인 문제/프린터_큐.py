# https://www.acmicpc.net/problem/1966

from collections import deque

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    tmp = list(map(int,input().split()))
    for i in range(n):
        if i == m:
            tmp[i] = (tmp[i],1)
        else:
            tmp[i] = (tmp[i],0)
    
    q = deque(tmp)
    cnt = 1
    while q:
        max_importance = max(q,key=lambda x: x[0])[0]
        paper = q.popleft()
        if paper[0] < max_importance:
            q.append(paper)
        else:
            if paper[1] == 1:
                print(cnt)
                break
            else:
                cnt+=1





