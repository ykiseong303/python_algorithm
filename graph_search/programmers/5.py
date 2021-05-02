'''
분류 : DFS & BFS
문제 : 게임 맵 최단거리 (프로그래머스)
작성일자 : 2021.05.02
'''

import sys
from collections import deque 
input = sys.stdin.readline

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

def solution (maps) : 
    answer = 0 
    dx, dy = [-1,1,0,0],[0,0,-1,1]
    r, c = len(maps), len(maps[0])
    # visit = [[0]*c for _ in range(r)]
    q = deque([(0,0)])
    # visit[0][0] = 1
    while q : 
        x, y = q.popleft()
        if x == r-1 and y == c-1 : 
            answer = maps[r-1][c-1] 
            return answer 
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0<=nx<r and 0<=ny<c) and maps[nx][ny] == 1 : 
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))
        # for m in maps : 
        #     print (*m)
    return -1

print(solution(maps))