'''
분류 : DFS & BFS
문제 : 순열 사이클 (백준 10451)
작성일자 : 2021.04.15
'''   

# 목적 : 순열 사이클의 수를 출력
# 접근 : 순열의 i번째(i>0보다 큰 정수)의 값을 1부터 ~ N까지 딕셔너리로 표현
#       이를 bfs를 수행하며 연결요소의 수를 출력
#       matrix로 돌리면 N이 최대 1000까지 이므로 메모리 초과가 발생할 수 있음
#       따라서 인접리스트로 구현

import sys 
from collections import deque 
input = sys.stdin.readline


def bfs(i) : 
    if visit[i] == 0 : 
        visit[i] = 1 
        q = deque([(i)])
        while q : 
            x = q.popleft()
            if visit[val[x]] == 0 : 
                visit[val[x]] = 1
                q.append((val[x]))
            # for j in val.key() : 


        return True 
    else : 
        return False 


T = int(input())
for _ in range(T) : 
    N = int(input())
    lst = list(map(int, input().split()))
    shape = [[0]*(N+1) for _ in range(N+1)]
    lst.insert(0,0)
    # dictionary로 풀이 
    val = {i : lst[i] for i in range(1,N+1)}
    visit = [0] * (N+1)
    count = 0 
    # for j in val.keys() : 
    #     print(j)
    for j in range(1,N+1) : 
        if bfs(j) == True : 
            count += 1 
    print(count)