# https://www.acmicpc.net/problem/10814

import sys
input = sys.stdin.readline
n = int(input())

members = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    members.append([age, name, i])


members.sort(key = lambda x: x[2])
members.sort(key = lambda x: x[0])

for member in members:
    print(member[0], member[1])