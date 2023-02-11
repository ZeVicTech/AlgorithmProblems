# https://school.programmers.co.kr/learn/courses/30/lessons/92342

# 이진수를 활용한 비트마스킹 기법을 처음 배워서 사용했다.
# 이진수를 사건이 일어난 경우와 일어나지 않는 경우를 각각 1과 0으로 매칭할 수 있다는 것을 배움

def solution(n, info):
    answer = [0] * 11
    tmp = [0] * 11
    maxDiff = 0
    
    for subset in range(1<<10):
        cnt = 0
        ryan = 0
        appeach = 0
        for i in range(11):
            if subset & (1<<i):
                ryan += 10-i
                tmp[i] = info[i] + 1
                cnt += tmp[i]
            else:
                tmp[i] = 0
                if info[i]:
                    appeach += 10-i
                    
        if cnt > n:
            continue
            
        tmp[10] = n - cnt
        
        if ryan-appeach == maxDiff:
            for i in reversed(range(11)):
                if tmp[i] > answer[i]:
                    answer = tmp[:]
                    break
                if tmp[i] < answer[i]:
                    break
            
        elif ryan-appeach > maxDiff:
            maxDiff = ryan-appeach
            answer = tmp[:]
            
    if maxDiff == 0:
        answer = [-1]
        
    return answer

solution(5,[2,1,1,1,0,0,0,0,0,0,0])