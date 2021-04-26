'''
분류 : DFS & BFS
문제 : 치즈 (백준 2636)
작성일자 : 2021.04.26
'''

# 목적 : 치즈가 모두 녹는 시간과 녹기 직전의 개수 출력
# 접근 : 공기 좌표들의 bfs수행
# 구현 : 1. 치즈 바깥의 공기와 치즈 안의 구멍의 별개처리
#       2. 치즈 녹이기 (공기좌표의 bfs)
#          >> 탈출 문제에서처럼, 큐의 길이만큼만 수행(1회씩처리)
#       3. 치즈를 녹인 후, 공기가 구멍을 만났을 때의 처리
#          >> 현재 공기의 좌표에서 구멍을 만나는 경우 bfs수행

import sys 
import copy
from collections import deque 
input = sys.stdin.readline

def bfs(air) : 
    global cnt, ans
    while air : 
        one_cnt = 0
        for s in shape : 
            for a in s : 
                if a == 1 : 
                    one_cnt += 1
        if one_cnt == 0 : 
            break
        ans.append(one_cnt)        
        len_air = len(air)
        while len_air : 
            x, y = air.popleft()
            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                if (0<=nx<N and 0<=ny<M) and shape[nx][ny] == 1 : 
                    shape[nx][ny] = 2
                    air.append((nx,ny))
            len_air -= 1

        # 1회 탐색 후, 구멍(0)을 만나는 경우 처리 
        temp = copy.deepcopy(air)
        while temp : 
            x, y = temp.popleft()
            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                if (0<=nx<N and 0<=ny<M) and shape[nx][ny] == 0 : 
                    shape[nx][ny] = 2
                    temp.append((nx,ny))
                    air.append((nx,ny))
        cnt += 1
        # print("\n")
        # for s in shape : 
        #     print(*s)
def find_air(x1,y1) : 
    global air
    shape[x1][y1] = 2
    q = deque([(x1,y1)])
    air.append((x1,y1))
    while q : 
        x, y = q.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0<=nx<N and 0<=ny<M) and shape[nx][ny] == 0 : 
                shape[nx][ny] = 2 
                q.append((nx,ny))
                air.append((nx,ny))

N, M = map(int, input().split())
shape = [list(map(int, input().split()))for _ in range(N)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
cnt, ans = 0, []
air = deque()
# 공기의 위치를 모두 2로 변환
find_air(0,0)
# 치즈 녹이기 시작
bfs(air)
print(cnt)
print(ans[-1])
