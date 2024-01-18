# https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline
n = int(input())

test = [input().rstrip() for _ in range(n)]

for sent in test:
    stack = []
    flag = 0
    for s in sent:
        if s == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                print('NO')
                flag = 1
                break
            else:
                stack.pop()
    
    if flag == 0:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
    
