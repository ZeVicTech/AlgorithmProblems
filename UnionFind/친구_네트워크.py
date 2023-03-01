# https://www.acmicpc.net/problem/4195

"""
다른 사람의 아이디어를 참고한 문제
다른 부분의 로직은 내가 직접 구현한게 맞았지만 사람의 수를 세는 것에서 시간초과가 났다.
처음에는 parent배열에서 같은 부모를 가지는 것들을 조회해서 카운트 했기 때문에 반복문 마다 시행하게 되면 시간복잡도가 O(n^2)이 된다.

해결방법은 새로운 딕셔너리를 이용하는 것이었다.(다른 사람의 아이디어 참고)
union함수를 시행할 때 마다 각각의 집합의 갯수를 더하는 방법을 통해 일일이 조회하지 않고도 사람의 수를 카운트 할 수 있다.
"""

import sys
n = int(sys.stdin.readline().rstrip())

# x는 문자열임
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(a,b,parent):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a > b:
        parent[a] = b
        cnt[b] += cnt[a]
        return b
    elif a < b:
        parent[b] = a
        cnt[a] += cnt[b]
        return a
    else:
        return a

for i in range(n):
    m = int(sys.stdin.readline().rstrip())
    parent = {}
    cnt = {}
    for j in range(m):
        a,b = sys.stdin.readline().rstrip().split()
        if a not in parent.keys():
            parent[a] = a
            cnt[a] = 1
        if b not in parent.keys():
            parent[b] = b
            cnt[b] = 1
        x = union(a,b,parent)

        print(cnt[x])
