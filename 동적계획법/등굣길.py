# https://school.programmers.co.kr/learn/courses/30/lessons/42898

# 최단경로의 경우 이동방향이 오른쪽과 아래로 가는 경우로만 이루어져야 됨


def solution(m, n, puddles):

    map = [[0 for i in range(m)] for j in range(n)]

    for i in range(m):
        if [i+1,1] in puddles:#물울덩이는 인덱스 시작값이 1이기 때문에 +1를 해줘야함
            break
        map[0][i] = 1

    for i in range(n):
        if [1,i+1] in puddles:
            break
        map[i][0] = 1

    for i in range(1,n):
        for j in range(1,m):
            if [j+1,i+1] in puddles:
                map[i][j] = 0
            else:
                map[i][j] = map[i-1][j] + map[i][j-1]

    return map[n-1][m-1]%1000000007

solution(4,3,[[2,2]])