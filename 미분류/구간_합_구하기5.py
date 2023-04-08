# https://www.acmicpc.net/problem/11660

"""
접두사 합을 활용해서 해결했다.
그냥 구간을 정해서 반복문을 돌경우 매번 반복문을 돌아야하기 때문에 시간 초과가 나온다.

개선해야 할점 나는 행을 기준으로만 접두사 합을 구했지만 행과 열 모두 고려해서 접두사 합을
구현한다면 좀더 효율적으로 해결할 수 있을 것이다.(적용완료)
"""

import sys
from pprint import pprint
input = sys.stdin.readline

n,m = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i][j-1] + maps[i-1][j-1]

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[j][i] = dp[j-1][i] + dp[j][i]

for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())

    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])