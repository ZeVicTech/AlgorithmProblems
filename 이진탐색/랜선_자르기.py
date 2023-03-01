# https://www.acmicpc.net/problem/1654

# 이분 탐색 이용
# 전형적인 이분탐색 문제, 기준을 무엇으로 잡느냐가 중요

import sys

k,n = map(int,input().split())
lines = [int(sys.stdin.readline()) for _ in range(k)]

start = 1
end = max(lines)

while start <= end:
    mid = (start+end)//2
    cnt = 0
    for line in lines:
        cnt += line//mid
    if cnt >= n:
        start = mid+1
        max_length = mid
    else:
        end = mid - 1

print(max_length)
