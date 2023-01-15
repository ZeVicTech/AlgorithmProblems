#https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    count = 0
    pri = []

    for index, item in enumerate(priorities):
        pri.append((item,index))

    queue = deque(pri)

    while True:
        doc = queue.popleft()
        if queue:
            max_pri = max(queue, key = lambda x : x[0])
        if doc[0] < max_pri[0]:
            queue.append(doc)
        else:
            count += 1
            if doc[1] == location:
                break
    return count

solution([1, 1, 9, 1, 1, 1],0)