from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    queue = deque(people)
    
    # 2명씩 탈 수 있으므로 정렬 후 양끝의 합이 limit를 넘지 않을 경우 보트 한대 추가
    # limit를 넘는 경우 가장 무거운 사람(start)가 혼자만 탄 경우로 보고 보트 한대 추가 후
    # 가벼운 사람은(end) 다시 큐에 추가 시킴
    # 결국 탈 수 있는 무게를 최대로 만드는 것이 관건임(그리디인 이유)
    while queue:
        start = queue.popleft()
        if len(queue) == 0:
            answer += 1
            break
        end = queue.pop()
        if start + end > limit:
            queue.append(end)
        answer += 1

    return answer


