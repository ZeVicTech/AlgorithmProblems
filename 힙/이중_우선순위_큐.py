# https://www.acmicpc.net/problem/7662

import heapq

n = int(input())

for _ in range(n):
    m = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * m
    for i in range(m):
        order,num = input().split()
        num = int(num)
        if order == 'I':
            heapq.heappush(min_heap,(num,i))
            heapq.heappush(max_heap,(-num,i))
            visited[i] = True
        else:
            if num == 1:
                while max_heap and visited[max_heap[0][1]] == False:
                    heapq.heappop(max_heap)
                if max_heap:
                    value = heapq.heappop(max_heap)
                    visited[value[1]] = False
            if num == -1:
                while min_heap and visited[min_heap[0][1]] == False:
                    heapq.heappop(min_heap)
                if min_heap:
                    value = heapq.heappop(min_heap)
                    visited[value[1]] = False
    
    while min_heap and visited[min_heap[0][1]] == False:
        heapq.heappop(min_heap)
    while max_heap and visited[max_heap[0][1]] == False:
        heapq.heappop(max_heap)

    if min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")

                




