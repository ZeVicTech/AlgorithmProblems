# https://www.acmicpc.net/problem/15657

n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
temp = []

def dfs(start):
    if len(temp) == m:
        print(" ".join(map(str,temp)))
        return
    for i in range(start,n):
        temp.append(lst[i])
        dfs(i)
        temp.pop()

dfs(0)