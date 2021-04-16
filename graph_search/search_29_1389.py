'''
분류 : DFS & BFS
문제 : 케빈 베이컨의 6단계 법칙 (백준 1389)
작성일자 : 2021.04.16
'''   

# 목적 : 케빈 베이컨 수가 가장 작은 정점 출력
# 접근 : 모든 정점에서 모든 정점으로의 최단 경로를 구하는 문제 
#       플로이드 워셜을 적용하여 풀이
#       bfs로도 풀이 가능


import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
# lst = [list(map(int, input().split()))for _ in range(M)]
# 각 정점을 표현하기 위한 매트릭스 생성
shape = [[10000]*(N) for _ in range(N)]
for _ in range(M) : 
    x, y = map(int, input().split())
    shape[x-1][y-1] = 1
    shape[y-1][x-1] = 1
for i in range(N) : 
    for j in range(N) : 
        if i==j : 
            shape[i][j] = 0 
for k in range(N) : 
    for i in range(N) : 
        for j in range(N) : 
            if shape[i][j] > shape[i][k] + shape[k][j] : 
               shape[i][j] = shape[i][k] + shape[k][j]
ans = []
index = 1
for s in shape : 
    ans.append([sum(s),index])
    # print(sum(s))
    index +=1 
ans.sort(key=lambda x : x[0])
print(ans[0][1])