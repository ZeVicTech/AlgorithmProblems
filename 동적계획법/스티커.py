# https://www.acmicpc.net/problem/9465

"""
다른 사람의 아이디어를 참고해서 해결한 문제
규칙을 정확히 찾아내는 것이 아직 미숙하다.
근접하게는 가는 것 같지만 좀 더 구체화 하는 부분이 미흡하다.
"""

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0] * n for i in range(2)]
    graph = [list(map(int,input().split())) for i in range(2)]

    for i in range(0,n):
        if i == 0:
            dp[0][0],dp[1][0] = graph[0][0],graph[1][0]
        elif i == 1:
            dp[0][i] = graph[0][i] + dp[1][i-1] # 위에 스티커가 선택된 경우
            dp[1][i] = graph[1][i] + dp[0][i-1] # 아래 스티커가 선택된 경우
        else:
            dp[0][i] = graph[0][i] + max(dp[1][i-1],dp[1][i-2]) # 위에 스티커가 선택된 경우
            dp[1][i] = graph[1][i] + max(dp[0][i-1],dp[0][i-2]) # 아래 스티커가 선택된 경우

    print(max(dp[0][n-1],dp[1][n-1]))

