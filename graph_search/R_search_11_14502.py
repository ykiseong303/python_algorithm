'''
분류 : DFS & BFS
문제 : 연구소 (백준 14502)
작성일자 : 2021.03.24
'''

# 목적 : 안전지대의 최대 칸수 구하기 
# 접근 : 벽 3개를 세울 수 있는 모든 경우에 대해 최대 안전지대를 구한다
#       벽 3개를 세우는 모든 경우 > 완전탐색을 통해 구현
#       바이러스가 퍼지는 것 > bfs를 통해 구현 
#       deepcopy를 통해 복사에 문제 없게 구현
#       벽을 세우는 경우를 조합을 통해서도 구현 가능 
#       조합 : https://bcp0109.tistory.com/entry/%EB%B0%B1%EC%A4%80-14502%EB%B2%88-%EC%97%B0%EA%B5%AC%EC%86%8C-Java-Python
import sys
import copy
from collections import deque

def bfs(q) : 
    global max_val
    result = 0
    # 원래의 맵을 copy한다 
    temp = [[0]*M for _ in range(N)] # 똑같은 크기를 0으로 채운다
    for i in range(N) : 
        for j in range(M) : 
            temp[i][j] = shape[i][j]
    # 바이러스 bfs를 수행한다 
    while q : 
        x, y = q.popleft()
        # print(x,y)
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M : 
                continue 
            if temp[nx][ny] == 0 : 
                temp[nx][ny] = 2
                q.append((nx, ny))
    # 0의 개수를 count  
    for t in temp : 
        for a in t : 
            if a == 0 : 
                result += 1
    max_val = max(max_val, result)
# 벽을 재귀적으로 생성한다 
def setWall (cnt) : 
    if cnt == 3 : # 벽이 3개가 지어지면
        q = copy.deepcopy(queue)
        # print(q)
        bfs(q) # 바이러스 bfs를 수행
        return 
    for i in range(N) : 
        for j in range(M) : 
            if shape[i][j] == 0 : # 0인 부분을 발견하면
                shape[i][j] = 1 # 벽을 세우고
                setWall(cnt+1) # 다음 벽을 세우기 위해 재귀호출
                # 마지막 재귀호출이 끝나면 가장 마지막에 세운 벽을 허문다
                shape[i][j] = 0
                # 이후 다시 직전단계의 재귀호출로 돌아가 반복문을 다시 수행한다 


# 1. 문제의 정보 받아오기 
N, M = map(int, input().split())
shape = []
for _ in range(N) : 
    shape.append(list(map(int, sys.stdin.readline().rstrip().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
max_val = 0 
for i in range(N) : 
    for j in range(M) : 
        if shape[i][j] == 2 : 
            queue.append((i,j))
# q = copy.deepcopy(queue)
# q.popleft()
# print(queue)
# print(q)
# 2. 벽 3개를 세울 수 있는 모든 경우를 만들기 
setWall(0)
print(max_val)