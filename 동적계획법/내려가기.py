# https://www.acmicpc.net/problem/2096

"""
전형적인 dp문제 하지만 메모리에 제한을 두어 dp테이블을 리스트로 만들어서 쓰지 못했고
변수를 선언하여 계속 돌려쓰는 방식을 취했다.
"""
import sys
input = sys.stdin.readline

n = int(input())

for i in range(0,n):
    x,y,z = map(int,input().split())
    if i == 0:
        l,m,r = x,y,z
        ll,mm,rr = x,y,z
    else:
        temp1 = x + max(l,m)
        temp2 = y + max(l,m,r)
        temp3 = z + max(m,r)

        l,m,r = temp1,temp2,temp3

        temp1 = x + min(ll,mm)
        temp2 = y + min(ll,mm,rr)
        temp3 = z + min(mm,rr)

        ll,mm,rr = temp1,temp2,temp3


print(max(l,m,r), min(ll,mm,rr))
