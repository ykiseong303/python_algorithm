'''
분류 : DFS & BFS
문제 : 섬의 개수 (백준 4963)
작성일자 : 2021.03.24
'''

# 목적 : 섬의 개수를 출력
# 접근 : 정보로 map이 나온 경우와 dfs를 이용한다
#       8각 방향을 고려한다 
#       1인 경우만 큐에 넣어서 bfs로 돌릴 수 없음 (현재위치의 4방향에 안닿는 곳이 있을 수 있음)

import sys
from collections import deque
sys.setrecursionlimit(10000)


def bfs(i,j) : 
    if shape[i][j] == 1 : 
        shape[i][j] = 0 
        queue = deque([(i,j)])
        while queue : 
            x, y = queue.popleft()
            for i in range(8) : 
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny<0 or nx>=h or ny>=w : 
                    continue
                if shape[nx][ny] == 1 : 
                    shape[nx][ny] = 0 
                    queue.append((nx,ny))
        return True
    else : 
        return False 

def dfs(i,j) : 
    if shape[i][j] == 1 : 
        # print("i,j",i,j)
        shape[i][j] = 0 
        for k in range(8) : 
            nx = i + dx[k]
            ny = j + dy[k]
            # print(nx, ny,k)
            if nx<0 or ny<0 or nx>=h or ny>=w : 
                continue
            if shape[nx][ny] == 1 : 
                # print("yes",nx,ny)
                dfs(nx,ny)
        return True 
    else : 
        return False 

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]
while 1 : 

    result = 0 
    shape = []
    count = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0 : 
        break
    for _ in range(h) : 
        shape.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for i in range(h) : 
        for j in range(w) : 
            if bfs(i,j) == True : 
                count += 1 
    print(count)
    