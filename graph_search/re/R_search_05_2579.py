'''
분류 : DFS & BFS
문제 : 연구소 (백준 14502)
작성일자 : 2021.06.24
'''

# 목적 : 최대 안전지대의 수를 출력
# 접근 : 벽을 하나씩 세워보고, 세개째 되었을 때 바이러스 bfs 이후 안전지대 count
#       모든 경우를 살펴보기 위하여 세웠던 벽을 허무는 과정 필요 (백트래킹)
#       원래의 shape, 바이러스 위치를 유지하기 위해 deepcopy 

import copy
import sys 
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
res = 0

def bfs() : 
    global res 
    virus = copy.deepcopy(q)
    new_shape = copy.deepcopy(shape)
    while virus : 
        x, y = virus.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M : 
                if new_shape[nx][ny] == 0 : 
                    new_shape[nx][ny] = 2 
                    virus.append((nx,ny))
    cnt = 0
    for n in new_shape : 
        for a in n :
            if a== 0 : 
                cnt += 1  
    res = max(res, cnt)

def setWall(cnt) : 
    if cnt == 3 : 
        bfs()
        return
    for i in range(N) : 
        for j in range(M) : 
            if shape[i][j] == 0 : 
                shape[i][j] = 1 
                setWall(cnt+1)
                shape[i][j] = 0 

N, M = map(int, input().split())
shape = [list(map(int, input().split()))for _ in range(N)]
q = deque()
for i in range(N) : 
    for j in range(M) : 
        if shape[i][j] == 2 : 
            q.append((i,j))
setWall(0)
print(res)