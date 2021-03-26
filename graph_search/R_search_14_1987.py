'''
분류 : DFS & BFS
문제 : 알파벳 (백준 1987)
작성일자 : 2021.03.25
'''

# 목적 : 같은 곳에 들리지 않고 갈 수 있는 최대 칸수
# 접근 : 탐색을 수행한 곳 중에서 이동칸수가 가장 많은 값을 출력한다
#       재귀의 마지막 호출에서 끝나는 경우 다른 경우를 위해 
#       백트래킹으로 이전의 값을 다시 원래대로 돌려주면서(방문기록을 없애면서)
#       다른 경우의 이동 칸수를 확인한다 
#       연구소 문제의 벽 쌓기와 같은 개념이다 
#       내일 다시 복습하고 bfs로도 풀어본다 

import sys 
sys.setrecursionlimit(10000)

def dfs(i,j,result) : 
    global answer
    answer = max(answer, result)
    for k in range(4) : 
        nx = i + dx[k]; ny = j+dy[k]
        if nx<0 or ny<0 or nx>=R or ny>=C : 
            continue
        if visit[shape[nx][ny]] == 0 : 
            visit[shape[nx][ny]] = 1 
            dfs(nx,ny,result+1)
            # 재귀 호출이 끝날때마다 
            # > 이 말은 마지막 재귀호출이 끝나면 순차적으로 끝나니깐
            # 해당호출에서의 방문기록을 다시 원래대로 돌린다 
            # 다음 nx,ny의 경우를 확인할 수 있게하기 위해서 
            visit[shape[nx][ny]] = 0

R, C = map(int, input().split())
shape = [list(map(lambda x:ord(x)-65, sys.stdin.readline().rstrip())) for _ in range(R)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0
visit = [0] * 26
visit[shape[0][0]] = 1 
dfs(0,0,1)
print(answer)