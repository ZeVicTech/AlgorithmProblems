# https://www.acmicpc.net/problem/11650
import sys
input = sys.stdin.readline
n = int(input())

numbers = [list(map(int,input().split())) for _ in range(n)]

numbers.sort(key = lambda x : x[1])
numbers.sort(key = lambda x : x[0])

for num in numbers:
    print(num[0], num[1])