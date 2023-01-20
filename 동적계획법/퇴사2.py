#https://www.acmicpc.net/problem/15486

# 다른 사람의 아이디어 보고 푼 문제
# 정말 해설을 봐도 이해가 잘 되지 않는 문제였다.
# 작은 문제를 어떻게 정의 해야할지 감이 잡히지 않았다.
# 해설을 본뒤 dp 값들을 업데이트 하는 방법도 직관적으로 이해가 되지 않았다.

n = int(input())
time = [0]
pay = [0]
for i in range(n):
    t,p = map(int,input().split())
    time.append(t)
    pay.append(p)

dp = [0]*(n+2)

#dp[i]는 i일 전까지 일했던 금액
for i in range(1,n+2):
    if dp[i] < dp[i-1]:
        dp[i] = dp[i-1]
    if i < n+1 and time[i] + i <= n+1:
        dp[i+time[i]] = max(pay[i]+dp[i],dp[i+time[i]])

print(dp[-1])


