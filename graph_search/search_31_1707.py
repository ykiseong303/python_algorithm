'''
분류 : DFS & BFS
문제 : 이분 그래프 (백준 1707)
작성일자 : 2021.04.18
'''   

# 목적 : 이분 그래프 여부를 확인해서 출력
# 접근 : bfs로 탐색, 한 정점에서 인접한 다른 정점을 서로 다른 그룹으로 분리
#       기준 정점과 인접한 항목의 그룹이 같다면 이분그래프가 성립되지 않음
#       그래프의 정점이 모두 연결되어 있지 않을 수도 있음에 유의

# 다른 풀이
# 직접 풀은 방법과 로직은 같으나, 두 그룹으로 분리하는 과정을 없앰
import sys 
from collections import deque 
input = sys.stdin.readline

def bfs(i) : 
    visit[i] = 1 
    q = deque([(i)])
    while q : 
        x = q.popleft()
        for j in adj_lst[x] : 
            # 기준 정점의 인접정점이 방문한적이 없다면
            if visit[j] == 0 : 
                # 기준 정점 값에 곱하기 -1 해서 저장
                visit[j] = -1 * visit[x]
                q.append((j))
            else : 
                # 방문한적이 있는 정점
                # 그런데 그 노드의 방문기록 값이 기준 정점의 방문기록 값과 같다면
                # 이분그래프가 되지 않으므로 return False 
                if visit[j] == visit[x] : 
                    return False 

T = int(input())
for _ in range(T) : 
    V, E = map(int, input().split())
    adj_lst = {i : [] for i in range(1,V+1)}
    visit = [0] * (V+1)
    for _ in range(E) : 
        x, y = map(int, input().split())
        adj_lst[x].append(y)
        adj_lst[y].append(x)
    flag = True 
    for i in range(1,V+1) : 
        if visit[i] == 0 : 
            if bfs(i) == False : 
                flag = False # 한번이라도 false뜨면 바로 종료
                break
    print("YES" if  flag else "NO")

'''
# 나의 풀이
import sys 
from collections import deque 
input = sys.stdin.readline

def bfs(node) : 
    global visit 
    global result
    R, B = [],[] 
    visit[node] = 1
    R.append(node)
    q = deque([(node,'R')])
    while q : 
        x, flag = q.popleft()
        # print(x,flag)
        for i in adj_lst[x] : 
            if flag == 'R' : 
                if i in R : 
                    result.append("N")
                    return
                else : 
                    if visit[i] == 0 : 
                        B.append(i) 
                        visit[i] = 1 
                        q.append((i,'B'))
            else : 
                if i in B : 
                    result.append("N")
                    return 
                else : 
                    if visit[i] == 0 :
                        R.append(i)
                        visit[i] = 1
                        q.append((i,'R'))
                    
    # print("YES")

T = int(input())
for _ in range(T) : 
    V, E = map(int, input().split())
    # if V == 1 : 
    #     print("NO")
    #     continue
    adj_lst = {i : [] for i in range(V+1)}
    visit = [0] * (V+1)
    for _ in range(E) : 
        x, y = map(int, input().split())
        adj_lst[x].append(y)
        adj_lst[y].append(x)
    # bfs(adj_lst)
    result = []
    for i in range(1,V+1) : 
        if visit[i] == 0 : 
            bfs(i)
    if 'N' in result : 
        print("NO")
    else : 
        print("YES")
'''