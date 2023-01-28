# https://school.programmers.co.kr/learn/courses/30/lessons/84512

# 다른사람의 아이디어를 보고 해결한 문제
# 간단한 문제였던것 같지만 발상을 제대로 떠올리지 못함

from itertools import product

def solution(word):
    result = []
    words = ['A','E','I','O','U']
    for i in range(1,6):
        for item in product(words,repeat=i):
            result.append(''.join(item))
    result.sort()
    return result.index(word) + 1

solution("AAAAE")