# https://www.acmicpc.net/problem/15655

n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
temp = []
visited = [0]*(n+1)
def dfs(start):
    if len(temp) == m:
        print(" ".join(map(str,temp)))
        return
    
    for i in range(start,n):
        if visited[i] == 0:
            temp.append(lst[i])
            visited[i] = 1
            dfs(i)
            temp.pop()
            visited[i] = 0

dfs(0)