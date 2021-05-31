'''
분류 : 다이나믹 프로그래밍
문제 : RGB거리 (백준 1149)
작성일자 : 2021.05.31
'''

# 목적 : 집을 모두 칠하는 최소비용 출력
# 접근 : ai = 현재위치의 값 + 이전위치들의 값 중 최솟값
#       조건 1 > 이전위치의 값으로 현재(다음)문제를 해결
#       조건 2 > 특정위치에서의 최소 비용값을 구하기 위해서는 맨처음에서부터의 계산을 반복해야함
# 구현 : 현재 행의 최솟값을 더하는 것이 무조건 최소비용이 될 수 없음(문제의 규칙때문에)
#       3열의 모든 경우의 수를 확인하고, 이를 기록하고 재사용하는 dp로 풀면서 시간초과를 방지

# 바텀업 방식(다른풀이, 입력받은 리스트를 dp테이블로 사용한 경우)
N = int(input())
shape = [list(map(int, input().split()))for _ in range(N)]
for i in range(1,N) : 
    shape[i][0] = shape[i][0] + min(shape[i-1][1],shape[i-1][2])
    shape[i][1] = shape[i][1] + min(shape[i-1][0],shape[i-1][2])
    shape[i][2] = shape[i][2] + min(shape[i-1][0],shape[i-1][1])
print(min(shape[N-1][0],shape[N-1][1],shape[N-1][2]))


# 바텀업 방식(dp테이블을 따로 사용한 경우)
'''import sys 
input = sys.stdin.readline

N = int(input())
shape = [list(map(int, input().split())) for _ in range(N)]
INF = sys.maxsize
d = [[INF]*3 for _ in range(N)]
d[0][0],d[0][1],d[0][2] = shape[0][0],shape[0][1],shape[0][2]
for i in range(1,N) : 
    for j in range(3) : 
        if j == 0 : 
            d[i][j] = min(d[i][j], shape[i][j] + min(d[i-1][j+1],d[i-1][j+2]))
        if j == 1 : 
            d[i][j] = min(d[i][j], shape[i][j] + min(d[i-1][j-1],d[i-1][j+1]))
        if j == 2 : 
            d[i][j] = min(d[i][j], shape[i][j] + min(d[i-1][j-1],d[i-1][j-2]))
res = INF
for i in range(3) : 
    res = min(res,d[N-1][i])
print(res)'''