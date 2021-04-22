'''
분류 : DFS & BFS
문제 : 인구이동 (백준 16234)
작성일자 : 2021.04.22
'''

# 목적 : 인구이동의 수를 출력
# 접근 : 그래프 탐색
# 구현 : 
##      1. 인구이동의 종료조건 
##      2. 인구이동의 횟수 출력
##      3. 그룹원의 수 count, 인구 재분배
##      4. 탐색조건 유의 : (L ~ R사이)
##      5. 방문처리 : 2차원 리스트 (map과 동일구조로)
import sys 
import math
from collections import deque 
input = sys.stdin.readline

def bfs(x1,y1) : 
    global flag
    # global cnt
    flag += 1
    # 현재 위치를 방문처리
    visit[x1][y1] = 1
    q = deque([(x1,y1)]) # 현재위치를 큐에 삽입
    group_cnt = 1 # 그룹 구성원의 수 
    total = shape[x1][y1] # 그룹 구성원의 합
    lst = deque() # 그룹 구성원의 좌표를 담을 리스트
    lst.append(([x1,y1]))
    while q : 
        x, y = q.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N :
                if (L<=abs(shape[x][y]-shape[nx][ny]) and abs(shape[x][y]-shape[nx][ny])<=R) and visit[nx][ny] == 0 : 
                    lst.append(([nx,ny]))
                    group_cnt += 1
                    total += shape[nx][ny]
                    visit[nx][ny] = 1
                    q.append((nx,ny))
    total = math.trunc(total/group_cnt)
    if len(lst) > 1 : 
        while lst : 
            a, b = lst.popleft()
            shape[a][b] = total
    return flag 


N, L, R = map(int, input().split())
shape = [list(map(int, input().split()))for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visit = [[0]*N for _ in range(N)]
flag = 0 # 한번의 반복에 인구이동이 일어났는지 확인하기 위한 변수
cnt = 0
while 1 : 
    # 종료 조건을 flag로 하지 않고
    # 인구 재분배를 bfs호출 아래로 끌고와서
    # 좌표를 담고 있는 리스트의 길이가 1초과인지 여부를 확인하면 됌
    visit = [[0]*N for _ in range(N)]
    flag = 0 # 한번 로직을 돌린 후, flag를 초기화
    for i in range(N) : 
        for j in range(N) : 
            if visit[i][j] == 0 : 
                bfs(i,j)
                     # flag는 방문하지 않은 지역에서 bfs를 수행할때 1 증가하므로,
    if flag == N*N : # flag가 N*N까지 증가했다면, 한번도 인구이동이 일어나지 않은 것
        print(cnt)
        break
    cnt += 1
