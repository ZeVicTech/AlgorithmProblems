# https://www.acmicpc.net/problem/11723

"""
비트 마스킹으로도 풀어볼 예정 23.06.24
"""

import sys
input = sys.stdin.readline

m = int(input())
s = [0 for _ in range(21)]

for _ in range(m):
    data = input().rstrip().split()

    if len(data) == 1:
        order = data[0]
    else:
        order = data[0]
        num = int(data[1])

    if order == 'add':
        s[num] = 1

    elif order == 'check':
        print(s[num])

    elif order == 'remove':
        s[num] = 0

    elif order == 'toggle':
        if s[num] == 0:
            s[num] = 1
        else:
            s[num] = 0

    elif order == 'all':
        s = [1 for i in range(21)]

    else: # empty
        s = [0 for i in range(21)]