import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic = {} # 데이터를 저장할 딕셔너리 생성

for _ in range(n):
    name = input().rstrip()
    if name in dic.keys():
        dic[name] += 1
    else:
        dic[name] = 1

for _ in range(m):
    name = input().rstrip()
    if name in dic.keys():
        dic[name] += 1
    else:
        dic[name] = 1

data = [item[0] for item in dic.items() if item[1] == 2]
data.sort()

print(len(data))
for d in data:
    print(d)
