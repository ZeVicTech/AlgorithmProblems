#https://school.programmers.co.kr/learn/courses/30/lessons/42895

# 다른사람의 아이디어를 참고해서 해결한 문제
# 작은 문제를 어떻게 정의할지에서 많이 헤맸던 것 같다.
# 되는 케이스를 하나씩 하나씩 적어보면서 분석하는 것이 좋겠다.
# 그리고 사칙연산을 조합할때 어떻게 순회할지에 대한 방법을 정하는데에도
# 좀 헤멨던 것 같다. 양 방향에서 서로 접근해오는 방식을 떠올렸어야 했다.

def solution(N, number):

    list = []

    for i in range(8):
        temp = set()
        temp.add(int(str(N)*(i+1)))
        for j in range(i):
            for x in list[j]:
                for y in list[-j-1]:
                    temp.add(x + y)
                    temp.add(x * y)
                    if y <= x:
                        temp.add(x - y)
                    if y != 0:
                        temp.add(x // y)
        if number in temp:
            print(i+1)
            return i+1
        list.append(temp)

    return -1

solution(5,31168)