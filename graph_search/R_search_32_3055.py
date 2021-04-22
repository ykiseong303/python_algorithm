'''
분류 : DFS & BFS
문제 : 탈출 (백준 3055)
작성일자 :  21.04.21
'''   

# 목적 : S가 목적지까지 도달하는 최단시간 출력
# 접근 : bfs를 통한 최단거리 출력
# 구현 : 
##      1. 물과 S의 큐를 구분 : 물이 이동할 곳으로 S가 이동하지 못하기 때문
##      2. 물과 S를 번갈아가며 수행 : 현재 큐에 담긴 값들까지만 수행
##         > 추가로 append되는건 다음에 수행
##         > 1번의 이유로 물의 이동을 먼저 1회 시작하고 bfs를 수행한다
##         > 물의 이동은 목적지와 X를 제외한 모두 갈 수 있으므로, 
#          > 처음 S의 위치를 .으로 바꾸고 시작
##      3. 피해야 하는 것들 구분
##      4. 방문처리 및 최단시간 표시 : 2차원 map그대로 
##         > 다음위치까지의 시간표현의 편리를 위해 첫번째 위치는 그냥 0으로 유지
##         > 어차피 목적지 도달과는 상관이 없음 (칸이 1개라면 그 자체이므로 0)
##      5. 종료조건 : S가 현재위치에서 더 이상 움직일 곳이 없거나(S의 큐가 빌때), 
##         > 목적지에 도달한 경우

import sys 
from collections import deque 
input = sys.stdin.readline

def bfs(x1,y1) : 
    # visit[x1][y1] = 0 # 현재 S의 위치를 방문처리
    q = deque([(x1,y1)]) # 현재 S의 위치를 큐에 삽입
    while q :
        # 물과 S의 이동을 번갈아가며 수행 
        # 번갈아가며 수행을 위해 물과 S는 현재 큐에 저장된 값까지만 탐색을 수행해야함
        # 추가로 append되는 값은 다음 턴에 수행
        lenq = len(q) 
        while lenq : 
            x, y = q.popleft()
            if shape[x][y] == 'D' : 
                print(visit[x][y])
                return 
            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                # 범위에 벗어나지 않고, 방문한적이 없는 곳이라면
                if (0<=nx<R and 0<=ny<C) and visit[nx][ny] == 0 :
                    if shape[nx][ny] == '.' or shape[nx][ny] == 'D':  
                        visit[nx][ny] = visit[x][y] + 1
                        q.append((nx,ny))
                    # elif shape[nx][ny] == 'D' : 
                    #     print(visit[x][y])
                    #     return
            lenq -= 1

        water_move()
        # print("\n")
        # for v in visit : 
        #     print(*v)
        # print("\n")
        # for s in shape : 
        #     print(*s)
    print("KAKTUS")
    return

def water_move() : 
    lenw = len(water)
    while lenw : 
        x, y = water.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0<=nx<R and 0<=ny<C) and shape[nx][ny] == '.': 
                shape[nx][ny] = '*'
                water.append((nx,ny))
        lenw -= 1 

R, C = map(int, input().split())
shape = [list(input().strip())for _ in range(R)] 
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 방문처리를 위한 리스트 생성
visit = [[0]*C for _ in range(R)]
# 현재 S와 물의 위치를 저장
q, water = deque(), deque()
for i in range(R) : 
    for j in range(C) : 
        if shape[i][j] == 'S' : 
            x1, y1 = i,j
            shape[i][j] = '.'
        elif shape[i][j] == '*' :
            water.append((i,j))
water_move()
# bfs를 수행
bfs(x1,y1)







'''
import sys 
from collections import deque 
input = sys.stdin.readline

def bfs(xi,yi) : 
    q.append((xi,yi))
    visit[xi][yi] = 1
    while q : 
        lenq = len(q) 
        while lenq : 
            x, y = q.popleft()
            # if shape[x][y] == 'D' : 
            #     return c[x][y] - 1 
            for i in range(4) : 
                nx, ny = x+dx[i],y+dy[i]
                if 0<=nx<R and 0<=ny<C : 
                    if shape[nx][ny] == '.' and visit[nx][ny] == 0 : 
                        visit[nx][ny] = visit[x][y] + 1 
                        q.append((nx,ny))
                    elif shape[nx][ny] =='D' : 
                        print(visit[x][y])
                        return 
            lenq -= 1
        water()
    print("KAKTUS")
    return

def water() : 
    wqlen = len(wq)
    while wqlen : 
        x, y = wq.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C : 
                if shape[nx][ny] == '.' : 
                    shape[nx][ny] = '*'
                    wq.append((nx,ny))
        wqlen -= 1

R, C = map(int, input().split())
shape = [list(input().strip())for _ in range(R)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 방문처리를 위한 리스트 생성
visit = [[0]*C for _ in range(C)]
# 현재 S와 물의 위치를 큐에 각각 대입
q,wq = deque(), deque()
for i in range(R) : 
    for j in range(C) : 
        if shape[i][j] == 'S' : 
            xi, yi = i,j
            shape[xi][yi] = '.' # 현재위치를 바로 방문처리할 것이므로 빈공간처리
        elif shape[i][j] == '*' :
            wq.append((i,j))
# visit[xi][yi] = 1 # S의 현재위치를 방문처리
water()
bfs(xi,yi)
'''

