# https://www.acmicpc.net/problem/6064

import sys
input = sys.stdin.readline

def cal_lcm(a,b): #최소 공배수 계산
    for i in range(1,b+1):
        if a*i % b == 0:
            return a*i


def check(x,y,lcm):
    cnt = 0

    while True:
        num = m*cnt + x
        ny = num%n

        if ny == 0:
            ny = n

        if ny == y:
            break

        if num > lcm:
            return -1
        
        cnt += 1

    return num


t = int(input())

for _ in range(t):
    m,n,x,y = map(int,input().split())
    lcm = cal_lcm(m,n)
    print(check(x,y,lcm))