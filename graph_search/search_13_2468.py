'''
분류 : DFS & BFS
문제 : 안전 영역 (백준 2468)
작성일자 : 2021.03.25
'''

# 목적 : 최대 안전 영역의 수를 출력 
# 접근 : 비가 와서 땅이 잠기는 모든 경우의 수 중 최대를 출력한다
#       브루트포스 + dfs(bfs)
#       비가 아예 오지 않을 수도 있다
#       어지간하면 bfs를 사용하기. dfs로 한다면 pypy로 바꿔보거나 
#       recursionlimit을 늘려보기 
import sys
import copy
sys.setrecursionlimit(10000)

def dfs(i,j,target) : 
    global temp
    # temp = copy.deepcopy(shape)
    if temp[i][j] > target : 
        temp[i][j] = target 
        for a in range(4) : 
            nx = i + dx[a]
            ny = j + dy[a]
            if nx<0 or ny<0 or nx>=N or ny>=N : 
                continue 
            if temp[nx][ny] > target : 
                # print(nx,ny)
                dfs(nx,ny,target)
        # for s in temp : 
        #     print(*s)
        # print("\n")
        return True 
    else : 
        return False 
        


N = int(input())
shape = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
max_h = max(map(max, shape))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0 
max_count = 0
temp = [] 
for k in range(0,max_h+1) : 
# for k in range(9,10) : 
    temp = copy.deepcopy(shape)
    count = 0
    for i in range(N) : 
        for j in range(N) : 
            if dfs(i,j,k) == True : 
                count += 1
                # print(count)
    max_count = max(max_count,count)
print(max_count)
