# https://www.acmicpc.net/problem/15652

n,m = map(int,input().split())

temp = []

def dfs(start):
    if len(temp) == m:
        print(" ".join(map(str,temp)))
        return
    
    for i in range(start,n+1):
        temp.append(i)
        dfs(i)
        temp.pop()

dfs(1)