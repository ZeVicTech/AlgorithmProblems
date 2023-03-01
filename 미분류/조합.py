# https://www.acmicpc.net/problem/2407

"""
알게된 점: 나누기를 할때 오차가 생길 수 있다는 것을 고려해야함
"""

from itertools import combinations

n,m = map(int,input().split())

def fac(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i

    return sum

answer = fac(n)//(fac(n-m)*fac(m))
print(answer)

