# https://school.programmers.co.kr/learn/courses/30/lessons/92335

#https://github.com/encrypted-def/kakao-blind-recruitment/blob/master/2022-blind/Q2.py
# 좀더 깔끔한 풀이

# 소수 판별하는 방법

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= n**0.5:
        if n%i == 0:
            return False
        i+=1
    return True

def solution(n, k):
    arr = []
    for i in range(1000000):
        if k**i > 1000000:
            break
        arr.append(k**i)
    
    arr.reverse()
    
    result = []
    
    for x in arr:
        if n >= x:
            result.append(str(n//x))
            n -= (n//x * x)
        else:
            result.append('0')
            
    result = ''.join(result)
    result = result.split('0')
    
    cnt = 0
    
    for item in result:
        if item == '':
            continue
        elif is_prime(int(item)):
            cnt += 1
            
    return cnt