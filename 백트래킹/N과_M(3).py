# https://www.acmicpc.net/problem/15651

"""
방문처리를 할 필요가 없었던 dfs
"""

n,m = map(int,input().split())

temp = []
def dfs():
    if len(temp) == m:
        print(" ".join(map(str,temp)))
        return
    
    for i in range(1,n+1):
        temp.append(i)
        dfs()
        temp.pop()

dfs()