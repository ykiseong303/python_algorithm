'''
분류 : DFS & BFS
문제 : 섬의 개수 (백준 4963)
작성일자 : 2021.03.24
'''

# 목적 : 섬의 개수를 출력
# 접근 : 대각선의 방향까지 고려해서 그래프탐색 (연결요소의 수)

import sys 
from collections import deque 

def bfs(i, j) : 
    if shape[i][j] == 1 : 
        shape[i][j] = 0 
        q = deque([(i,j)])
        while q :
            x, y = q.popleft()
            for k in range(8) : 
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<h and 0<=ny<w : 
                    if shape[nx][ny] == 1 : 
                        shape[nx][ny] = 0 
                        q.append((nx,ny))
        return True 
    else : return False 

while 1 : 
    w, h = map(int, input().split())
    if w == 0 and h == 0 : break 
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]

    shape = [list(map(int, input().split()))for _ in range(h)]
    count = 0
    for i in range(h) : 
        for j in range(w) : 
            if bfs(i,j) == True : 
                count += 1 
    print(count)

