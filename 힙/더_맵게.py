# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    
    heap = scoville[:]
    heapq.heapify(heap)
    cnt = 0
    
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        food1 = heapq.heappop(heap)
        food2 = heapq.heappop(heap)

        food = food1 + 2*food2

        heapq.heappush(heap,food)
        cnt += 1

    return cnt

solution([1, 2, 3, 9, 10, 12],7)