# https://www.acmicpc.net/problem/15666

n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
visited = [0]*(n)

temp = []
def dfs(start):
    if len(temp) == m:
        print(" ".join(map(str,temp)))
        return
    prev = -1
    for i in range(start,n):
        if prev == lst[i]:
            continue
        temp.append(lst[i])
        dfs(i)
        prev = temp.pop()

dfs(0)

