# https://school.programmers.co.kr/learn/courses/30/lessons/87946

import itertools

def solution(k, dungeons):
    answer = 0

    lst = itertools.permutations(dungeons,len(dungeons))
    for item in lst:
        hp = k
        cnt = 0
        for cost in item:
            if hp >= cost[0]:
                hp -= cost[1]
                cnt += 1
            else:
                break
        answer = max(answer, cnt)

    return answer

solution(80,([80,20],[50,40],[30,10]))