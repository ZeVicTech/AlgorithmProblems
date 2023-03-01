# https://www.acmicpc.net/problem/9019

# 접근방법과 구현은 거의 맞았지만 문제중 회전 조건을 잘못이해함
# 시프트연산의 특징을 잘 생각해봐야됨

from collections import deque

n = int(input())
test = [list(map(int,input().split())) for _ in range(n)]

def d(n):
    temp = 2*n
    if temp > 9999:
        return temp%10000
    else:
        return temp

def s(n):
    if n == 0:
        return 9999
    else:
        return n-1

def l(n):
    temp = str(n)
    if len(temp) == 1:
        temp = "000"+temp
    elif len(temp) == 2:
        temp = "00"+temp
    elif len(temp) == 3:
        temp = "0"+temp
    answer = temp[1:]
    answer += temp[0]

    return int(answer)

def r(n):
    temp = str(n)
    if len(temp) == 1:
        temp = "000"+temp
    elif len(temp) == 2:
        temp = "00"+temp
    elif len(temp) == 3:
        temp = "0"+temp
    answer = temp[:-1]
    answer = temp[-1] + answer

    return int(answer)

def bfs(start):
    visited = [0]*10000
    order = ["" for _ in range(10000)]
    q = deque()
    q.append(start)
    visited[start] = 1

    func = ["D","S","L","R"]

    while q:
        v = q.popleft()

        for i in range(4):
            if i == 0:
                nv = d(v)
            elif i == 1:
                nv = s(v)
            elif i == 2:
                nv = l(v)
            else:
                nv = r(v)

            if visited[nv] == 0:
                q.append(nv)
                visited[nv] = 1
                order[nv] = order[v] + func[i]
    
    return order

for x,y in test:
    answer = bfs(x)
    print(answer[y])            

