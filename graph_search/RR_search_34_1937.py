'''
분류 : DFS & BFS
문제 : 욕심쟁이 판다 (백준 1937)
작성일자 : 2021.04.22
'''

# 목적 : 판다가 최대 버틸 수 있는 일수 출력
# 접근 : DFS + DP
#       큰 문제의 해답에 작은 답이 포함되어 있는경우
#       접근 방법이나 문제 구현자체는 쉬우나 시간초과의 문제가 발생한다
#       따라서 시간을 줄이기 위해 DP를 사용하는데
#       어떤 특정위치에서 다른 곳까지 갈 수 있는 최댓값을 기록(memo)
#       그러면 다음에 다른 위치에서 아까 그 위치에 다시 들릴 때,
#       더 이상 진행할 필요 없이 기록해둔 값을 받아 사용할 수 있음
#       재귀호출을 사용하되 한 번 사용한 것은 메모함으로써 중복호출을 피한다


import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x1,y1) : 
    if memo[x1][y1] : # 초기 값이 0이 아닌 다른 값인경우(이미 방문한경우)
        return memo[x1][y1] # 그 자리의 값을 그대로 리턴한다
    memo[x1][y1] = 1 # 방문한적이 없다면 그 위치에서 하루 버틸 수 있으므로 1을 저장
    for i in range(4) : 
        nx, ny = x1+dx[i],y1+dy[i]
        if 0<=nx<N and 0<=ny<N : 
            # 현재 위치보다 다음 목적지의 값이 크다면
            if shape[x1][y1] < shape[nx][ny] : 
                # 현재 기록해둔 값과, 재귀를 통해 불러오는 값을 비교한다
                # +1을 하는 이유는, 현재 위치에서 바로 인접한위치까지는
                # 어쨌든 1번은 이동해야하기 때문에
                memo[x1][y1] = max(memo[x1][y1], dfs(nx,ny)+1)
    # 현재위치에 기록된 값을 리턴한다
    return memo[x1][y1]


N = int(input())
shape = [list(map(int, input().split()))for _ in range(N)]
dx, dy = [-1,1,0,0],[0,0,-1,1]
memo = [[0]*N for _ in range(N)] # 이전 값을 기록하기 위한 DP리스트 생성
max_val = 0
result = 0
for i in range(N) : 
    for j in range(N) :
        result = dfs(i,j)
        max_val = max(max_val, result)
print(max_val)