# https://www.acmicpc.net/problem/20529

import sys
from itertools import combinations

input = sys.stdin.readline

def distance(x,y): # 매개변수로 받은 mbti의 심리적 거리 계산
    sum = 0
    for i in range(4):
        if x[i] != y[i]:
            sum+=1

    return sum

t = int(input())

for _ in range(t):
    n = int(input())
    mbti = input().rstrip().split()

    if n > 32: # 32개 초과일 경우 적어도 동일한 mbti를 가진 사람이 3명이상 존재하게 됨(비둘기집 원리)
        print(0)
        continue

    mbti = list(combinations(mbti,3)) # 조합을 이용해 3명씩 묶는 모든 경우를 찾음
    min_value = int(1e9)
    for m in mbti:
        total = 0
        total += distance(m[0],m[1])
        total += distance(m[1],m[2])
        total += distance(m[0],m[2])
        min_value = min(total, min_value)

        if min_value == 0: # min_value가 0이면 이보다 적을 수 없으므로 조기종료
            break

    print(min_value)


