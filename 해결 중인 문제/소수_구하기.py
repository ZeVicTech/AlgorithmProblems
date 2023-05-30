# https://www.acmicpc.net/problem/1929
import math

m,n = map(int,input().split())

def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x == 2:
            return True
        elif x%i == 0:
            return False
    return True

for i in range(m,n+1):
    if is_prime(i):
        print(i)
