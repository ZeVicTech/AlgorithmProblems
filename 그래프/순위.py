# https://school.programmers.co.kr/learn/courses/30/lessons/49191

# 다른 사람의 아이디어를 보고 해결한 문제
# 순위 결정되는 조건을 파악하지 못했다.
# 왜 파악하지 못했나?
# 기본적인 조건을 보기보다 어떤 그래프 알고리즘을 적용할지 고민했다.
# 먼저 예시를 도식화하여 당연한 것이라고 생각할지라도 명확하게 정리해야한다.
# 순위가 결정되려면 모든 인원에 관한 승패기록이 존재해야함
# a가 b를 이기고 b가 c를 이기면 a는 c를 이긴 것이됨
# 이렇게 직접적으로 결과가 주어지진 않은 것들도 승패 기록을 찾아내려면 플로이드 워셜을 사용하면 됨
# 이긴것만 기록 하면 되느냐? 아니다 진것도 기록을 해야한다.

from pprint import pprint

def solution(n, results):
    INF = int(1e9)
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for a,b in results:
        graph[a][b] = 1
        graph[b][a] = -1
    
    for i in range(1,n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 1
                
    pprint(graph)
                
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    
    answer = 0
    
    pprint(graph)
    
    for i in range(1,n+1):
        if 0 in graph[i][1:]:
            continue
        answer += 1
                
    
    return answer