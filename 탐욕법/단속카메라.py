# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    routes.sort(key = lambda x : x[0])
    std = routes[0][1]
    answer = 1 #기준 하나당 카메라가 1개 필요한데 우리는 기준을 잡고 시작한므로 1개가 기본으로 필요하다.
    for i in range(1,len(routes)):
        if std < routes[i][0]:
            answer += 1
            std = routes[i][1]
        else:
            std = min(routes[i][1],std)

    return answer

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])

# 처음에 이 문제를 풀기 위해 카메라가 설치되어야하는 정확한 위치를 선정하려고 했다.
# -30,000 에서 30,000 까지의 범위에서 카메라가 각각 설치 되어 있다고 가정하고
# 최대한 많은 차량의 경로가 지나가는 지점의 카메라를 선택하려고 했다.
# 하지만 이 해결방법은 카메라 커버 하지 못하는 차량의 경로가 생길 수 있기 때문에 해결하기
# 쉽지 않아서 다른 접근 방법을 생각해야 했다. 도저히 생각이 나지 않아 결국 다른 사람들의 
# 아이디어를 참고했다.

# 1. 해결방법은 routes를 진입점으로 오름차순 정렬한 뒤 첫번째 경로의 진출점을 기준으로 다음에 
# 오는 경로들의 진입점을 비교하는 것이다. 
# 2. 다음에 오는 경로가 기준 보다 작을 경우 그 경로는 
# 겹쳐있다고 볼 수 있다. 여기서 해당 경로의 진출점이 기준보다 작은 경우 기준을 해당 
# 경로의 진출점으로 업데이트 해준다. 왜냐하면 이같은 경우 해당 경로가 기준의 경로에 포함되는 
# 상태인데 여기서 진입점은 기준의 진출점 보다 작지만 해당경로의 진출점보다는 큰 경로가 올 경우 
# 기준의 경로 범위안에 서로 겹치지 않는 두개의 경로가 존재하게 된다. 
# 이 경우 카메라 하나로 커버가 불가능하다.
# 3. 다음에 오는 경로의 진입점이 기준보다 큰 경우에는 겹쳐 있지 않기 때문에 기준을 해당 경로의 진출점으로 
# 업데이트 한 후 카메라 수를 1개 더해주고 다음 경로와 비교를 반복한다. 

# 내가 왜 잘못된 방법으로 접근했을까??
# 나는 탐욕법 문제에 너무 매몰되어 가장 최선의 값(여기서는 경로가 중복되는 횟수)을
# 찾는 방법을 잘못 생각했던것 같다. 주어진 정보에 좀 더 주목해야할 필요가 있어보인다.