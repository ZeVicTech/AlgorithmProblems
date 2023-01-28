# https://www.acmicpc.net/problem/12865

# 다른 사람의 아이디어를 참고한 문제 (냅색문제)
# 참고한 블로그 https://claude-u.tistory.com/208

n,k = map(int, input().split())
lst = [[0,0]]#더미 추가

for i in range(n):
    lst.append(list(map(int,input().split())))

dp = [[0 for j in range(k+1)] for i in range(n+1)]

for i in range(1,n + 1):
    for j in range(1,k + 1):#j는 가방 무게
        weight = lst[i][0]
        value = lst[i][1]

        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight],dp[i-1][j])

print(dp[n][k])


