# https://school.programmers.co.kr/learn/courses/30/lessons/42861

# 크루스칼 알고리즘을 활용해서 해결해야함

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solution(n, costs):
    parent = [i for i in range(n)]

    costs.sort(key = lambda x: x[2])

    sum = 0

    for a,b,cost in costs:
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a != b:
            union_parent(parent,a,b)
            sum += cost

    return sum


solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
