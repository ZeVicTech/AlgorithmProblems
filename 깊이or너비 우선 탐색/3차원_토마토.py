# https://www.acmicpc.net/problem/7569

# 이번문제를 풀면서 알게된 정보
# sys.stdin.readline() 함수를 쓰면 더 빨리 읽을 수 있다.
# max함수의 경우 다차원 배열의 경우 맨앞의 원소값을 비교하여 대소를 판단한다.(값이 같으면 다음원소를 비교)

import sys
from collections import deque

def bfs(queue,box,m,n,h):

    dx = [1,0,0,-1,0,0]
    dy = [0,1,0,0,-1,0]
    dz = [0,0,1,0,0,-1]

    while queue:
        ori_z,ori_y,ori_x = queue.popleft()

        for i in range(6):
            x = ori_x + dx[i]
            y = ori_y + dy[i]
            z = ori_z + dz[i]

            if 0<=x<m and 0<=y<n and 0<=z<h:
                if box[z][y][x] == 0:
                    queue.append((z,y,x))
                    box[z][y][x] = box[ori_z][ori_y][ori_x] + 1
    
m,n,h = map(int,input().split())

box = [[] for _ in range(h)]

for i in range(h):
    for j in range(n):
        box[i].append(list(map(int,sys.stdin.readline().split())))

queue = deque()
flag = 0 #0이 유지 될경우 모든 토마토가 익은 경우

for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                queue.append((z,y,x))
            if box[z][y][x] == 0:
                flag = 1

answer = 0

if flag == 0:
    print(0)
else:
    bfs(queue,box,m,n,h)
    for a in box:
        for b in a:
            for c in b:
                if c == 0:
                    print(-1)
                    exit(0)
            answer = max(answer,max(b))
    print(answer-1)