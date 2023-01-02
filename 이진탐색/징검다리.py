#https://school.programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    start = 0
    end = distance

    rocks.sort()#바위를 위치순으로 정렬
    rocks.append(distance)#도착지점을 추가함

    while start <= end:
        mid = (start + end)//2
        print(mid)
        standard = 0
        num = 0
        for rock in rocks:
            between = rock - standard
            if mid <= between:
                standard = rock
            else:
                num += 1
        
        if num > n:
            end = mid - 1
        else:
            answer = mid#다른 사람들의 풀이를 보면 여기서 미드가 꼭 거리의 최솟값이라는 보장이 없다고 생각해서 돌거리 최소값을 따로 갱신해 주는 경우가 있음
            start = mid + 1
      
    return answer

solution(25,[2, 14, 11, 21, 17],2)