#https://school.programmers.co.kr/learn/courses/30/lessons/42746

from functools import cmp_to_key

def compare(x, y):
    a = x+y
    b = y+x

    if int(a) > int(b):
        return -1
    elif int(a) < int(b):
        return 1
    else:
        return 0
    # return 음수 : 먼저 들어온 요소가 앞으로 정렬됨
    # return 0 : 바뀌지 않음
    # return 양수 : 나중에 들어온 요소가 앞으로 정렬됨(먼저들어온 요소보다 앞에 배치됨)

def solution(numbers):
    numbers = list(map(str, numbers))

    numbers = sorted(numbers, key=cmp_to_key(compare))

    answer = str(int(''.join(numbers)))
    return answer