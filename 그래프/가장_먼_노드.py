# https://school.programmers.co.kr/learn/courses/30/lessons/49189


# 문제의 로직은 틀리지 않았는데 시간 초과가 떠서 헤멨던 문제
# 방문된 노드를 visited 리스트에 직접 추가하는 방법을 썼었는데
# 이러면 연결된 노드르 순회할때마다 visited리스트 안에 있는 요소들을 전부 순회 해야했다.
# 그래서 visited를 노드 개수 만큼 0으로 초기화하고 방문했을 경우 인덱스로 접근해서 1로 바꿔주는
# 방법을 선택했다.


from collections import deque

def bfs(graph, visited, start,route_cnt):

    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        value = queue.popleft()
        for node in graph[value]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = 1
                route_cnt[node] = route_cnt[value] + 1

def solution(n, edge):

    graph = [[] for _ in range(len(edge)+1)]
    route_cnt = [0]*(n+1)
    visited = [0] * (n+1)

    for v1,v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    bfs(graph, visited, 1, route_cnt)

    print(route_cnt.count(max(route_cnt)))
    return route_cnt.count(max(route_cnt))

solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])




