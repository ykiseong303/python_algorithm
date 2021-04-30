'''
분류 : DFS & BFS
문제 : 여행 가자 (백준 1976)
작성일자 : 2021.04.28
'''

# 목적 : 여행경로가 가능한지 출력
# 접근 : 여행경로가 1개의 연결요소와 동일한지 파악
#       같은 도시를 재방문하는 것이 가능하므로, 
#       여행경로가 가능하다면 탐색한 경로에 모두 있어야 한다
#       도시는 있는데, 연결된 곳이 한 곳도  없는 경우도 고려 
#       > 한번이라도 가능하다면 통과

# 플로이드워셜, 유니온파인드로도 가능
import copy
import sys 
from collections import deque 
input = sys.stdin.readline

def bfs(start) : 
    global result
    q = deque([(start)])
    visit[start] = 1 
    while q : 
        x = q.popleft()
        result.append(x)
        for i in range(N) : 
            if shape[x][i] == 1 and visit[i] == 0 : 
                visit[i] = 1
                q.append((i))
                

N = int(input())
M = int(input())
shape = [list(map(int, input().split()))for _ in range(N)]
target = list(map(int, input().split()))
visit = [0] * (N)
result = []
flag = False 
for i in range(N) : 
    if visit[i] == 0 : 
        bfs(i)
        temp = copy.deepcopy(target)
        while temp : 
            x = temp.pop()
            if x-1 not in result : 
                # 계속 맞다가 마지막 항에서 틀릴 수 있으므로(이미 pop된 상태이므로)
                temp.append(x) 
                break
        if len(temp) == 0 : # 한번이라도 제대로 통과했다면 큐의 길이는 0
            print("YES")
            sys.exit()
        temp = []
            # flag = True 

        # for t in target : 
        #     if t-1 not in result : 
        #         print("NO")
        #         sys.exit()
    result = []
print("NO")


