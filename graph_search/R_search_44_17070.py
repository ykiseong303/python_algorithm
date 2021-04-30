'''
분류 : DFS & BFS
문제 : 파이프 옮기기1 (백준 17070)
작성일자 : 2021.04.30
'''

# 목적 : 파이프의 한쪽을 목적지까지 도달시키는 경우의 수 출력
# 접근 : 
#       1. dfs로 모든 경우를 확인하며 목적지 도달할때마다 count
#           > 파이프의 끝위치만 고려
#           > 대각선인 경우 2*2만큼의 위치 확보 고려
#           > 방문처리는 필요하지 않은듯 : 아마도 다시 거슬러올라가는 경우는 없기 때문인듯(전진만 가능)
#           > bfs로 풀면 가지치기를 해줘도 시간초과
#       2. DP로 경로 테이블을 구하여 출력
#           > memo[d][x][y]는 x,y를 d방향으로 올 수 있는 경우의 수 
#       팬더문제는 다음 방문위치가 방문된적이 있는지 체크하며 재귀호출(하나씩 내려가기) - 탑다운
#       이 문제는 전진하면서 다음 위치를 만들어가는 방식(시작>목표로 하나씩 올라가기) - 바텀업
# DP를 이용한 풀이
import sys 
N = int(input())
shape = [list(map(int, input().split()))for _ in range(N)]
# memo[d][x][y] = x, y를 d방향으로 올 수 있는 경우의 수
# d = 0 : 가로, d = 1 : 세로, d = 2 : 대각선
memo = [[[0] * N for _ in range(N)]for _ in range(3)]
memo[0][0][1] = 1 # 0,1을 가로방향으로 올 수 있는 경우(시작이므로 1)
# 시작위치에서 가로방향으로 갈 수 있는 모든 경우를 다 구하기
for i in range(2,N) : 
    if shape[0][i] == 0 :
        memo[0][0][i] = memo[0][0][i-1]
# 시작위치에서부터 대각선 방향으로 갈 수 있는 모든 경우의 수 
## 시작할때 가로 방향으로 있었으므로, 가로와 대각선만 구하면 됌
for i in range(1,N) : 
    for j in range(2,N) : 
        # 대각선으로 이동하는 경우에는 2*2칸의 공간 확보
        if shape[i][j-1] == 0 and shape[i-1][j] == 0 and shape[i][j] == 0 : 
            memo[2][i][j] = memo[0][i-1][j-1] + memo[1][i-1][j-1] + memo[2][i-1][j-1]
        # 대각선이 아닌 가로, 세로 방향인 경우
        # 가려는 목적지가 0이면 가능
        if shape[i][j] == 0 : 
            # 가로에서 가로, 대각선에서 가로
            # ex) 1,2는 0,1에서 가로로 이동해서 1,1, 0,0에서 대각선으로 이동해서1,1
            # 이후 1,1에서 가로로 이동하면 1,2
            memo[0][i][j] = memo[0][i][j-1]+memo[2][i][j-1] 
            # 세로에서 세로, 대각선에서 세로
            memo[1][i][j] = memo[1][i-1][j]+memo[2][i-1][j]
print(memo[0][N-1][N-1]+memo[1][N-1][N-1]+memo[2][N-1][N-1])
'''
import sys 
from collections import deque 
input = sys.stdin.readline

def bfs(x,y,dir) : 
    global count 
    if x == N-1 and y == N-1 : 
        count += 1 
        return count
    q = deque([(x,y,dir)])
    while q : 
        x,y,d = q.popleft()
        # if x == N-1 and y == N-1 : 
        #     count += 1 
        if d == 0 :
            if y+1<N and shape[x][y+1] == 0 :
                if x == N-1 and y+1 == N-1 : 
                    count += 1 
                else : 
                    q.append((x,y+1,0))
            if x+1<N and y+1<N : 
                if shape[x][y+1] == 0 and shape[x+1][y] == 0 and shape[x+1][y+1] == 0 :
                    if x+1 == N-1 and y+1 == N-1 : 
                        count += 1 
                    else : 
                        q.append((x+1,y+1,2))
        if d == 1 : 
            if x+1<N and shape[x+1][y] == 0 :
                if x+1 == N-1 and y == N-1 : 
                    count += 1 
                else :
                    q.append((x+1,y,1))
            if x+1<N and y+1<N : 
                if shape[x][y+1] == 0 and shape[x+1][y] == 0 and shape[x+1][y+1] == 0 :
                    if x+1 == N-1 and y+1 == N-1 : 
                        count += 1 
                    else :
                        q.append((x+1,y+1,2))
        if d == 2 : 
            if y+1<N and shape[x][y+1] == 0 :
                if x == N-1 and y+1 == N-1 : 
                    count += 1 
                else :
                    q.append((x,y+1,0))
            if x+1<N and shape[x+1][y] == 0 :
                if x+1 == N-1 and y == N-1 : 
                    count += 1 
                else :
                    q.append((x+1,y,1))
            if x+1<N and y+1<N : 
                if shape[x][y+1] == 0 and shape[x+1][y] == 0 and shape[x+1][y+1] == 0 :
                    if x+1 == N-1 and y+1 == N-1 : 
                        count += 1 
                    else :
                        q.append((x+1,y+1,2))

def dfs(x,y,dir) :
    global count  
    if x==N-1 and y==N-1 :
        count += 1
    if dir == 0 : # 가로
        # 다시 가로로 이동 
        if y+1<N and shape[x][y+1] == 0 : # 가로방향일때는 y만 움직이므로 
            dfs(x,y+1,0)
        # 대각선 방향 이동
        if x+1<N and y+1<N : 
            if shape[x][y+1] == 0 and shape[x+1][y] == 0 and shape[x+1][y+1] == 0 : 
                dfs(x+1,y+1,2)
    if dir == 1 : # 세로
        # 다시 세로로 이동
        if x+1<N and shape[x+1][y] == 0 :
            dfs(x+1,y,1)
        if x+1<N and y+1<N : 
            if shape[x][y+1] == 0 and shape[x+1][y] == 0 and shape[x+1][y+1] == 0 : 
                dfs(x+1,y+1,2)
    if dir == 2 : # 대각선
        # 가로
        if y+1<N and shape[x][y+1] == 0 : # 가로방향일때는 y만 움직이므로 
            dfs(x,y+1,0)
        # 세로
        if x+1<N and shape[x+1][y] == 0 :
            dfs(x+1,y,1)
        # 다시 대각선
        if x+1<N and y+1<N : 
            if shape[x][y+1] == 0 and shape[x+1][y] == 0 and shape[x+1][y+1] == 0 : 
                dfs(x+1,y+1,2)


N = int(input())
shape = [list(map(int, input().split()))for _ in range(N)]
count = 0
#dfs(0,1,0)
bfs(0,1,0)
print(count)'''