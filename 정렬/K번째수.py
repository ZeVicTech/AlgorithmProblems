#https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):

    answer = []

    for start,end,pick in commands:
        print(start,end,pick)

        answer.append(sorted(array[start-1:end])[pick-1])

    print(answer)
    return answer