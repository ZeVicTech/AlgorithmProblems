# https://school.programmers.co.kr/learn/courses/30/lessons/92341

# 기본적인 구현문제이다.
# math 모듈의 ceil() 올림, floor() 내림. trunc() 버림을 알게됨
# round함수의 경우 반올림이지만 소수점 부분이 0.5의 경우 반올림 되는게 아닌 짝수로 반올림 혹은 반내림이 됨

import math

def solution(fees, records):
    dic = {}
    answer = []

    for record in records:
        time, car_num, io = record.split()
        if car_num not in dic.keys():
            dic[car_num] = []
            dic[car_num].append((time,io))
        else:
            dic[car_num].append((time,io))
            
    dic = sorted(dic.items())
    
    print(dic)
            
    for element in dic:
        result = []
        for i,item in enumerate(element[1]):
            h,m = map(int, item[0].split(':'))
            if i%2 == 0:
                result.append(-(h*60+m))
            else:
                result.append(h*60+m)
                
        if len(result)%2 == 1:
            result.append(23*60+59)
        
        total = sum(result)
        
        if total > fees[0]:
            cost = fees[1] + math.ceil((total - fees[0])/fees[2]) * fees[3]
        else:
            cost = fees[1]
        
        answer.append(cost)
            
    return answer