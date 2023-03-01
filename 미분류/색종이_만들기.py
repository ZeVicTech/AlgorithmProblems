# https://www.acmicpc.net/problem/2630

# 전형적인 쿼드 트리 문제이다.
# 나는 재귀함수로 구현했다. 처음에는 x,y의 시작점과 끝점을 파라미터로 받아 계산하려고 했다.
# 이럴 경우 x//2 연산에서 부정확한 값을 리턴하는 경우가 생김 (2,3)여기서 끝점인 3을 //2 연산을 할경우 1로 변함
# 그래서 사이즈를 파라미터로 받아서 size로 시작점을 표현했다
# pypy3를 쓸 경우 시간초과가 일어났지만 python3로 돌리니까 통과가능했다.
# 특정부분에서 pypy3가 메모리를 더 잡아먹는 경우가 있다고 한다.(대신 python3보다 빠른편이다)


import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt_1 = 0
cnt_0 = 0

def cut_paper(x, y, size):
    global cnt_1
    global cnt_0

    if color_check(x,y,size) == 1:
        cnt_1+=1
        return
    elif color_check(x,y,size) == 0:
        cnt_0+=1
        return
    
    size = size//2

    cut_paper(x, y, size)
    cut_paper(x+size, y, size)
    cut_paper(x, y+size, size)
    cut_paper(x+size, y+size, size)


def color_check(x, y, size):
    temp = []
    for i in range(x,x+size):
        for j in range(y,y+size):
            temp.append(graph[i][j])

    if 1 in temp and 0 in temp:
        return 2
    elif 1 in temp:
        return 1
    else:
        return 0

cut_paper(0,0,n)

print(cnt_0)
print(cnt_1)



