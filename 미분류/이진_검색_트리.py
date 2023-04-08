# https://www.acmicpc.net/problem/5639

"""
다른 사람의 아이디어를 참고해서 해결한 문제
처음에는 전위순회로 트리를 구현해서 문제를 풀었는데 시간초과가 났다.
전위순회의 특징을 고려해서 재귀로 구현해야했다.
전위순회로 얻은 리스트의 첫번째는 루트 노드이고 루트노드보다 작은 것들은 왼쪽 서브트리
루트노드보다 큰 것들은 오른쪽 서브트리를 구성하고 있으므로 이를 이용해서 재귀적으로 순회를 구현하면 된다.
"""

import sys
sys.setrecursionlimit(10**7)

node_list = []

while True:
    try:
        node_list.append(int(sys.stdin.readline()))
    except:
        break

def postorder(start,end):
    if start > end:
        return
    
    root = node_list[start]
    mid = end + 1 # mid의 초기값은 오른쪽 서브트리가 없다고 가정

    for i in range(start+1, end+1): # 루트보다 큰 값을 mid값으로 설정하기위한 반복문
        if node_list[i] > root:
            mid = i
            break
    
    postorder(start+1,mid-1)
    postorder(mid,end)
    print(root)

postorder(0,len(node_list)-1)




# import sys
# sys.setrecursionlimit(10**7)

# node_list = []
# tree = dict()

# while True:
#     try:
#         num = int(sys.stdin.readline())
#         node_list.append(num)
#     except:
#         break

# def make_tree(root,node):
#     if root > node:
#         if tree[root][0] == 0:
#             tree[root][0] = node
#             tree[node] = [0,0]
#         else:
#             make_tree(tree[root][0],node)
#     elif root < node:
#         if tree[root][1] == 0:
#             tree[root][1] = node
#             tree[node] = [0,0]
#         else:
#             make_tree(tree[root][1],node)

# def postorder(node):
#     left,right = tree[node][0],tree[node][1]
#     if left != 0:
#         postorder(left)
#     if right != 0:
#         postorder(right)
#     print(node)

# tree[node_list[0]] = [0,0]

# for node in node_list[1:]:
#     make_tree(node_list[0],node)

# postorder(node_list[0])
