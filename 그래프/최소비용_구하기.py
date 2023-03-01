# https://www.acmicpc.net/problem/1916

# 전형적인 다익스트라 문제
# 다익스트라를 구현하는데 힙에서 빼온 노드의 거리가 distance리스트에 있는 거리보다 클경우 무시해야한다는 조건을
# 떠올리지 못해 시간초과가 났었다.

import heapq
import sys
INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,dist = map(int,sys.stdin.readline().split())
    graph[a].append((b,dist))

start, end = map(int,sys.stdin.readline().split())
distance = [INF] * (n+1)

def dijkstra(start):

    distance[start] = 0

    heap = []
    heapq.heappush(heap,(0,start))

    while heap:
        dist, city = heapq.heappop(heap)

        if dist > distance[city]:
            continue
        for node in graph[city]:
            new_distance = dist + node[1]
            if new_distance < distance[node[0]]:
                distance[node[0]] = new_distance
                heapq.heappush(heap,(distance[node[0]],node[0]))

dijkstra(start)
print(distance[end])