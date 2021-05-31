'''
분류 : DFS & BFS
문제 : DFS와 BFS (백준 1260)
작성일자 : 2021.05.30
'''

# 목적 : 토마토가 모두 익는 최단시간 출력
# 접근 : 시작시점에서 익어있는 모든 토마토의 좌표를 큐에 넣고 bfs수행

import sys 
from collections import deque
input = sys.stdin.readline

def bfs() : 
    while q : 
        x, y = q.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i] 
            if 0<=nx<N and 0<=ny<M and shape[nx][ny] == 0 : 
                shape[nx][ny] = shape[x][y] + 1
                q.append((nx,ny))
    for s in shape : 
        if 0 in s : 
            return -1 
    res = max(map(max, shape))
    return res-1

M, N = map(int, input().split())
shape = [list(map(int, input().split()))for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 시작 시점에서 익은 토마토의 위치를 큐에 저장
q = deque()
for i in range(N) : 
    for j in range(M) : 
        if shape[i][j] == 1 : 
            q.append((i,j))
print(bfs())