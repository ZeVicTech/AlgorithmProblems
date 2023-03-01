# https://www.acmicpc.net/problem/1931

# 다른 사람의 아이디어를 참고한 문제
# 처음에 그리디로 접근해서 회의 소요시간을 기준으로 정렬하면 되지 않을까 생각했다.
# 하지만 그럴경우 최적의 해를 구할 수 없었고 냅색 같은 dp알고리즘이라고 생각했다.
# 결국은 끝값을 기준으로한 그리디 문제였다.
# 왜 그리디인 것을 놓쳤을까?
# 그리디의 기준을 좀더 다양하게 생각해보지않고 소요시간만을 기준으로 삼았기 때문이다.
# 알게된 것 키값으로 정렬 할때 키값만 참고해서 정렬 한다. 키값을 제외한 다른 값은 영향을 미치지 않는다.


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

arr.sort(key = lambda x: x[0])
arr.sort(key = lambda x: x[1])

answer = []
for item in arr:
    if len(answer) == 0:
        answer.append(item)
    elif answer[-1][1] <= item[0]:
        answer.append(item)

print(len(answer))
