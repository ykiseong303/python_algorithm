'''
분류 : 다이나믹 프로그래밍
문제 : 정수 삼각형 (백준 1932)
작성일자 : 2021.06.01
'''

# 목적 : 위에서 아래로 점수를 합해서 내려올 때 최댓값을 출력
# 접근 : 현재위치는 현재의 대왼, 대오의 합 중 최대값으로 갱신한다
#       단, 외곽에 위치한 경우는 다르게
# 구현 : 입력받을 때 N*N크기의 이중 리스트로 만들 수 있게 여백을 채우기
#       어차피 열의 index j가 i의 값에 의존하므로 굳이 채울 필요는 없음
N = int(input())
lst = []
for _ in range(N) : 
    lst.append(list(map(int, input().split())))
    # temp = list(map(int, input().split()))
    # temp_len = len(temp)
    # zero = [-1] * (N-temp_len)
    # temp.extend(zero)
    # lst.append(temp)
for i in range(1,N) : 
    for j in range(i+1) : 
        if j == 0 : 
            lst[i][j] = lst[i][j] + lst[i-1][j]
        elif j == i : 
            lst[i][j] = lst[i][j] + lst[i-1][j-1]
        else : 
            lst[i][j] =  lst[i][j] + max(lst[i-1][j-1],lst[i-1][j])
res = -1
for i in range(N) : 
    res = max(res,lst[N-1][i])
print(res)
