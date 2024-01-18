# https://www.acmicpc.net/problem/1620
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic = {}
arr = [0] #0은 더미 데이터

for i in range(1,n+1):
    name = input().rstrip()
    dic[name] = i
    arr.append(name)

for _ in range(m):
    data = input().rstrip()
    if '0' <= data[0] <= '9':
        print(arr[int(data)])
    else:
        print(dic[data])

