# https://www.acmicpc.net/problem/14500

# dfs 응용문제

import sys

n,m = map(int,input().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(graph)