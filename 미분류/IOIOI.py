# https://www.acmicpc.net/problem/5525

# 처음에는 이중 반복문을 통해 매번 p의 길이마다 비교해서 답을 구함 <- 시간초과
# 두번째는 조건에 만족할때마다 리스트에 넣어 조건이 깨질때 리스트 안에 몇번 반복되는지 확인하는 방법 구현하기 복잡해짐
# 세번째는 다른 사람의 아이디어를 참고했는데 반복되는 문자열만을 체크해서 넘어가는 방법이다.

# 이번 문제를 풀면서 알게된 새로운 사실
# 슬라이싱을 이용할 경우 끝 범위가 리스트의 최대 길이를 넘어가도 인데스 에러가 일어나지 않고
# 리스트의 끝 부분까지 반환해준다.

n = int(input())
m = int(input())
s = input()

#p = "I"+"OI"*n
# cnt = 0
# for i in range(m):
#     flag = 0
#     if i + len(p) - 1 < m:
#         for j in range(len(p)):
#             if s[i+j] != p[j]:
#                 flag = 1
#                 break
#         if flag == 0:
#             cnt += 1

i = 0
cnt = 0
answer = 0
while i < m-1:
    if s[i:i+3] == "IOI":
        cnt +=1
        i+=2
        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        i+=1
        cnt = 0

print(answer)
    
