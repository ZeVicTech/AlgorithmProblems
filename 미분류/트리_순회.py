# https://www.acmicpc.net/problem/1991

n = int(input())

tree = dict()

for i in range(n):
    p,l,r = input().split()
    tree[p] = [l,r]

# 전위 순회 함수
def pretrav(start):
    left = tree[start][0]
    right = tree[start][1]
    print(start, end="")
    if left != '.':
        pretrav(left)
    if right != '.':
        pretrav(right)

# 중위 순회 함수
def intrav(start):
    left = tree[start][0]
    right = tree[start][1]
    if left != '.':
        intrav(left)
    print(start, end="")
    if right != '.':
        intrav(right)

# 후위 순회 함수
def posttrav(start):
    left = tree[start][0]
    right = tree[start][1]
    if left != '.':
        posttrav(left)
    if right != '.':
        posttrav(right)
    print(start, end="")

pretrav('A')
print()
intrav('A')
print()
posttrav('A')
