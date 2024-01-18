# https://www.acmicpc.net/problem/18870
import sys
input = sys.stdin.readline

n = int(input())
coordinate = list(map(int,input().split()))

temp = sorted(list(set(coordinate))) # nlogn

dic = {}
for i,t in enumerate(temp): # n
    dic[t] = i

for c in coordinate: # n
    print(dic[c], end = ' ')
