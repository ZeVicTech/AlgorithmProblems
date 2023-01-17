# https://school.programmers.co.kr/learn/courses/30/lessons/86971

#개선시킬 수 있는 방안
#제약조건을 활용 해야한다.
#하나의 트리 형태로 주어진다는 것을 이용
#dfs를 이용해서 한번 순회하면 다른 그래프는 순회할 필요 없이 총 송전탑의 갯수에서 빼주면 된다.

# def solution(n, wires):
#     wires.sort(key = lambda x : x[0])
#     visited = [0] * (n+1)
#     graph_origin = [[] for _ in range(n+1)]
#     result = []
#     node_result = []
    
#     for v1,v2 in wires:
#         graph_origin[v1].append(v2)
#         graph_origin[v2].append(v1)

#     for v1,v2 in wires:
#         graph = [item[:] for item in graph_origin]
#         graph[v1].remove(v2)
#         graph[v2].remove(v1)
#         visited = [0] * (n+1)
#         result.clear()
#         for i in range(1,n+1):
#             if visited[i] == 1:
#                 continue
#             stack = [i]
#             node_cnt = 0
#             while stack:
#                 value = stack.pop()
#                 if visited[value] == 0:
#                     visited[value] = 1
#                     node_cnt += 1
#                 for tower in graph[value]:
#                     if visited[tower] == 0:
#                         stack.append(tower)
#             result.append(node_cnt)
#         node_result.append((max(result),min(result)))
#         print(node_result)

#     answer = min(v1 - v2 for v1,v2 in node_result)

#     print(answer)

#     return answer

# 개선점 반영
def DFS(del_wire, n, graph, visited):
    cnt = 0 #스택에서 pop되면서 방문처리 할 것이기 때문에 초깃값은 0
    stack = [del_wire[0]]
    visited_list = visited[:]
    while stack:
        value = stack.pop()
        if visited_list[value] == 0:
            visited_list[value] = 1
            cnt += 1
        for tower in graph[value]:
            if visited_list[tower] == 1 or tower == del_wire[1]:
                continue
            stack.append(tower)
    return cnt
 

def solution(n, wires):
    visited = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    result = n
    
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for wire in wires:
        temp = DFS(wire, n, graph, visited)
        result = min(result, abs(n - 2 * temp))

    print(result)

    return result

solution(4,[[1,2],[2,3],[3,4]])