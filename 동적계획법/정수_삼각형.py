# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    
    list = [item[:] for item in triangle]
    
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            temp = triangle[i][j] + list[i+1][j]
            triangle[i+1][j] = max(temp,triangle[i+1][j])
            
            temp = triangle[i][j] + list[i+1][j+1]
            triangle[i+1][j+1] = max(temp,triangle[i+1][j+1])
            
    answer = max(triangle[len(triangle)-1])
    
    return answer