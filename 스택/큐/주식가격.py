# https://school.programmers.co.kr/learn/courses/30/lessons/42584

# 스택을 활용하는 문제접근법까지는 맞았지만 시간을 계산하는 방법에서 애먹음
# 시간은 인덱스를 활용하여 구하는 방법을 생각했어야한다.

def solution(prices):
    answer = [i for i in range(len(prices) - 1 ,-1,-1)]
    
    
    stack = [0]
    for i in range(1,len(prices)-1):
        while stack:
            index = stack[-1]
            if prices[index] > prices[i]:
                answer[index] = i - index
                stack.pop()
            else:
                break
        stack.append(i)

    return answer