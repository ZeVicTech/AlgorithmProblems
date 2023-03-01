# https://www.acmicpc.net/problem/15663

"""
시간초과까지는 아니지만 실행시간이 느린편이라 개선점을 찾아보다가 구글링을 통해 아이디어를 얻음
직접 경우의 수를 그리며 규칙을 찾는게 중요하고 그것을 어떻게 구현할 것인지 생각하는게 중요함
"""

n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
visited = [0]*(n)

temp = []
def dfs():
    if len(temp) == m:
        print(" ".join(map(str,temp)))
        return
    prev = -1
    for i in range(n):
        if visited[i] == 1 or prev == lst[i]:
            continue
        temp.append(lst[i])
        visited[i] = 1
        dfs()
        prev = temp.pop()
        visited[i] = 0

dfs()

