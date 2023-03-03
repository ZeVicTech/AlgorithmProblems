# https://www.acmicpc.net/problem/1629

"""
다른 사람의 아이디어를 참고해서 해결한 문제
분할정복법을 이용해야하는 문제였다.
나머지 분배 법칙을 알아야 풀 수 있었다.
"""

a,b,c = map(int,input().split())

def func(a,b):
    if b == 1:
        return a%c
    
    if b%2 == 1:
        return ((func(a,b//2)**2)*a)%c
    else:
        return (func(a,b//2)**2)%c
    
print(func(a,b))
