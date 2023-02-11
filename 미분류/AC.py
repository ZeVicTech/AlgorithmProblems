# https://www.acmicpc.net/problem/5430

# .strip()함수를 알면 더 쉽게 풀었을 문제
# 처음에 시간초과가 일어나서 왜 그런지 고민 했는데 reverse가 시간 복잡도 O(N)을 가지고 있어
# 명령어 배열의 인자마다 reverse가 일어날 경우 O(N^2)의 시간복잡도를 기대하게됨


import sys
from collections import deque

def func(order,result):
    is_reverse = False

    for i in order:
        if i == 'R':
            is_reverse = not is_reverse
        elif i == 'D':
            if result:
                if is_reverse == True:
                    result.pop()
                else:
                    result.popleft()
            else:
                return 'error'

    if is_reverse == True:
        result.reverse()

    answer = ','.join(result)

    return '['+answer+']'

n = int(sys.stdin.readline())

for _ in range(n):
    order =(sys.stdin.readline())
    size = int(sys.stdin.readline())
    arr =(sys.stdin.readline())
    result = deque()
    tmp = []

    for i in arr:
        if ord('0') <= ord(i) <= ord('9'):
            tmp.append(i)
        else:
            if tmp:
                result.append(''.join(tmp))
                tmp = []

    print(func(order,result))