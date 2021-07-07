'''
분류 : DFS & BFS
문제 : 토마토 (백준 7569)
작성일자 : 2021.07.08
'''

# 목적 : 토마토가 익는 최단시간 출력
# 접근 : bfs + 위아래의 이동을 어떻게 구현할 것인지?
#       익은 토마토의 위치를 미리 큐에 넣어놓고  bfs를 수행 
#       왜냐하면 최단 시간을 찾아야 하기 때문 

import sys 
from collections import deque 
input = sys.stdin.readline

def bfs() : 
    while q : 
        x,y,z = q.popleft()
        for i in range(6) : 
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0<=nx<N and 0<=ny<M and 0<=nz<H : 
                if shape[nz][nx][ny] == 0 : 
                    shape[nz][nx][ny] = shape[z][x][y] + 1 
                    q.append((nx,ny,nz))

    res = 0
    for k in range(H) : 
        for i in range(N) : 
            for j in range(M) : 
                if shape[k][i][j] == 0 : 
                    return -1
                res = max(res, shape[k][i][j])
    return res-1

M, N, H = map(int, input().split())
shape = [[list(map(int, input().split())) for _ in range(N)]for _ in range(H)] 
q = deque()
dx, dy, dz = [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1]
for k in range(H) : 
    for i in range(N) : 
        for j in range(M) : 
            if shape[k][i][j]== 1 : 
                q.append((i,j,k))
print(bfs())
