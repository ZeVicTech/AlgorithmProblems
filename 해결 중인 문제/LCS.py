# https://www.acmicpc.net/problem/9251

n = int(input())

human = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    cnt = 1
    for j in range(n):
        if human[i][1] < human[j][1] and human[i][0] < human[j][0]:
            cnt += 1
    human[i].append(cnt)

for man in human:
    print(man[2])