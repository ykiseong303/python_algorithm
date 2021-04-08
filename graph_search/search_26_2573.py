'''
분류 : DFS & BFS
문제 : 빙산 (백준 2573)
작성일자 : 2021.04.08
'''   

# 목적 : 빙산이 두덩어리 이상으로 나눠지는 최소시간 출력
# 접근 : 빙산의 연결요소를 count하고, 2보다 작으면 빙산을 녹인다

from collections import deque
import sys 
import copy

def bfs(i,j,temp) : 
    if temp[i][j] != 0 : 
        q = deque([(i,j)])
        # 현재 위치를 방문처리 
        temp[i][j] = 0
        while q : 
            x, y = q.popleft()
            for k in range(4) : 
                nx, ny = x+dx[k], y+dy[k]
                if (0<=nx<N and 0<=ny<M) and temp[nx][ny] != 0 :
                    temp[nx][ny] = 0 
                    q.append((nx,ny))
        return True
    else : 
        return False 

def bingsan() : 
    global shape
    year = 0 
    while 1 : 
        count = 0 # 연결요소의 수 count
        zero = 0 
        temp = copy.deepcopy(shape) # 원래의 맵을 복사
        for i in range(N) : 
            for j in range(M) : 
                if bfs(i,j,temp) == True :
                    count += 1 
        for s in shape:
            for a in s : 
                if a == 0 :
                    zero +=  1
        if count >= 2 : 
            return year
        if zero == N*M and count < 2 : 
            return 0
        sea = 0
        temp_lst = copy.deepcopy(shape)
        for i in range(N) : 
            for j in range(M) : 
                if shape[i][j] != 0 : 
                    # 네방향으로 0의 개수를 count 
                    for k in range(4) : 
                        nx, ny = i+dx[k], j+dy[k]
                        # 범위를 벗어나지 않는 하에 
                        if (0<=nx<N and 0<=ny<M) and shape[nx][ny] == 0 : 
                            sea += 1
                    temp_lst[i][j] -= sea
                    if temp_lst[i][j] <= 0 : 
                        temp_lst[i][j] = 0
                    sea = 0 
        shape = copy.deepcopy(temp_lst)
        # for s in shape : 
        #     print(*s)
        # print("\n")
        year += 1



N, M = map(int, input().split())
shape = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
print(bingsan())