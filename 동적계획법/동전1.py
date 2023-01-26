# acmicpc.net/problem/2293

# 다른 사람의 아이디어를 참고해서 푼 문제
# 규칙성을 찾기 어려웠다.
# 규칙을 찾을 때 일단 어느정도 범위까지 시뮬레이션을 돌려서 결과를 보고
# 관찰해서 규칙을 찾아 점화식을 세워야 한다.

n,k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [0] * (k+1)
dp[0] = 1 #가치합이 0인 경우는 동전을 사용하지 않고도 만들 수 있음

for coin in coins:
    for i in range(k+1):
        if coin <= i:
            dp[i] += dp[i-coin]

print(dp[-1])



