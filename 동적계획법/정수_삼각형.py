# https://www.acmicpc.net/problem/1932 <- 백준
# https://school.programmers.co.kr/learn/courses/30/lessons/43105 <- 프로그래머스

"""
프로그래머스 문제 풀이

def solution(triangle):

    list = [item[:] for item in triangle]

    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            temp = triangle[i][j] + list[i+1][j]
            triangle[i+1][j] = max(temp, triangle[i+1][j])

            temp = triangle[i][j] + list[i+1][j+1]
            triangle[i+1][j+1] = max(temp, triangle[i+1][j+1])

    answer = max(triangle[len(triangle)-1])

    return answer

"""

# 백준 문제 풀이

n = int(input())

grpah = [list(map(int,input().split())) for _ in range(n)]
dp = [([0]*i) for i in range(1,n+1)]
dp[0][0] = grpah[0][0]

for i in range(0,n-1):
    for j in range(len(grpah[i])):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + grpah[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + grpah[i+1][j+1])

print(max(dp[n-1]))
