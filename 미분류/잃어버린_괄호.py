# https://www.acmicpc.net/problem/1541

"""
다른 사람의 아이디어를 참고해서 해결한 문제
처음 문제를 봤을때 어떻게 해결해야할지 감이 안잡혔다.
그래서 선택한 것이 숫자 리스트로 변환후 슬라이싱을 통해 완전탐색을 하려고 했으나 오답이 나왔다.
그래서 구글링을 통해 최솟값이 나오려면 -부호가 나왔을때 다음 -부호가 나오기 전까지의 숫자를 괄호로 묶으면 되는 것이었다.
나는 왜 생각을 못했을까?
최적의 해를 보장하는 방법이 없을 것이라고 너무 일찍 단정한 것과 괄호를 중복해서 써도 되는 것인지 판단을 못했다.
"""

exp = input().split('-')

answer = 0
for i in range(len(exp)):
    if i == 0:
        temp = list(map(int,exp[i].split('+')))
        answer = sum(temp)
    else:
        temp = list(map(int,exp[i].split('+')))
        answer -= sum(temp)

print(answer)
