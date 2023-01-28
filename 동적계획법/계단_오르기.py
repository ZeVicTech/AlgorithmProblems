# https://www.acmicpc.net/problem/2579


# 다른 사람의 아이디어를 참고해서 해결한 문제
# 어느정도 정답에 접근 했지만 해결은 못했다.
# dp 테이블 만 사용한다는 생각은 버려야 된다.
# 그리고 점화식을 세워야 하는데 기본예제를 보고 시뮬레이션을 여러번 돌리면서 파악을 해야겠다.

n = int(input())
point = [0]
for _ in range(n):
    point.append(int(input()))
dp = [0] *  (n + 1)

sum = point[n]
for i in range(1,n+1):
    if i == 1:
        dp[i] = point[i]
    elif i == 2:
        dp[i] = point[i] + dp[i-1]
    else:
        dp[i] = max(point[i] + point[i-1] + dp[i-3], point[i] + dp[i-2])



print(dp[n])