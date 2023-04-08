# https://www.acmicpc.net/problem/15686

"""
bfs를 활용해서 해결했지만 치킨집과 집의 거리를 구하는 방법은 굳이 bfs를 사용할 필요가 없었다.
최소거리라는 말을 듣고 bfs만을 떠올렸는데 다른 방법도 있다는 것을 명심해야한다.
bfs 이용하지 않는 방법으로 업데이트 했음
"""
import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
chick = []
houses = []
result = int(1e9)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chick.append((i,j))
        elif graph[i][j] == 1:
            houses.append((i,j))

combs = combinations(chick, m)

for comb in combs:
    sum = 0
    for house_x, house_y in houses:
        temp = int(1e9)
        for chick_x, chick_y in comb:
            temp = min(temp, abs(house_x - chick_x) + abs(house_y-chick_y))
        sum += temp
    result = min(result,sum)

print(result)