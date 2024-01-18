# https://school.programmers.co.kr/learn/courses/30/lessons/77885?language=python3

numbers=[2,7]

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        x = numbers[i]
        temp = 1
        while True:
            if x%2 == 0:
                if temp == 1:
                    answer.append(numbers[i]+temp)
                else:
                    answer.append(numbers[i]+temp-temp//2)
                break
            x = x//2 
            temp *= 2

    return answer

print(solution(numbers))