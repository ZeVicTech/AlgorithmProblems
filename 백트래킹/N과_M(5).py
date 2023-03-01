# https://www.acmicpc.net/problem/15654

n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
temp = []
visited = [0]*(n+1)

def dfs():
    if len(temp) == m:
        print(" ".join(map(str,temp)))
        return
    
    for i in range(1,n+1):
        if visited[i] == 0:
            temp.append(lst[i-1])
            visited[i] = 1
            dfs()
            temp.pop()
            visited[i] = 0

dfs()