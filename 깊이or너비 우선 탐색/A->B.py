# https://www.acmicpc.net/problem/16953

"""
bfs적용했지만 메모리 초과가 났던 문제
방문을 처리하기 위해 목표 숫자의 최댓값 크기의 리스트를 선언했는데 그 크기가 너무 컸기 때문임
그래서 방문처리를 하기위해 
"""

from collections import deque,defaultdict

a,b = map(int,input().split())
visited = []
cal_cnt = defaultdict(lambda: -1)

def bfs(start):
    q = deque()
    q.append(start)
    visited.append(start)
    cal_cnt[start] = 1

    while q:
        value = q.popleft()

        num = 2*value
        if num <= b and num not in visited:
            q.append(num)
            cal_cnt[num] = cal_cnt[value] + 1
        
        num = 10*value + 1
        if num <= b and num not in visited:
            q.append(num)
            cal_cnt[num] = cal_cnt[value] + 1

bfs(a)
print(cal_cnt[b])
