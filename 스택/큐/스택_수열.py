# https://www.acmicpc.net/problem/1874

"""
못 풀었던 이유: 수열이 만들어지지 않는 경우를 제대로 파악하지 못했다.
pop이 된 값은 반드시 seq의 원소와 매칭이 되어야 한다.
만약 매칭이 안된 채 그냥 pop이 되어버리면 그 값이 seq리스트에 남아있게 된다.

피드백: 문제를 먼저 제대로 이해한 후에 코딩에 들어가자
"""

import sys
input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]
stack = []
answer = []

flag = 0
cur = 1
for i in range(n):
    num = seq[i]

    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur+=1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for item in answer:
        print(item)

