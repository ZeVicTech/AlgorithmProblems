# https://www.acmicpc.net/problem/11053

"""
다른 사람의 아이디어를 참고한 문제
dp문제
아직까지 dp문제는 익숙하지 않은 것 같다.
시간복잡도를 생각하며 dp를 적용하는게 어려운 것 같다.
"""

n = int(input())
lst = list(map(int,input().split()))

dp = [1]*(n)

for i in range(1,n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))