# https://www.youtube.com/watch?v=acqm9mM1P6o&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 55:22

# 다익스트라 알고리즘을 처음으로 구현해서 문제를 풀었음

import heapq
def dijkstra(start,graph,distance):
    heap = []
    heapq.heappush(heap,(0,start))
    distance[start] = 0

    while heap:
        dist,now = heapq.heappop(heap)
        if dist > distance[now]:
            continue

        for item in graph[now]:
            cost = dist + item[0]
            if cost < distance[item[1]]:
                distance[item[1]] = cost
                heapq.heappush(heap,(cost,item[1]))

INF = int(1e9)

n,m,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((z,y)) # (전달되는 시간, 도착하는 도시)으로 저장

dijkstra(c,graph,distance)

cnt = -1

for i in distance:
    if i != INF:
        cnt += 1
print(cnt)

time = 0
for i in distance:
    if i != INF:
        time = max(time,i)

print(time)




