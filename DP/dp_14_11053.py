'''
분류 : 다이나믹 프로그래밍
문제 : 가장 긴 증가하는 부분 수열(백준 11053)
작성일자 : 2021.06.01
'''

# 목적 : 가장 긴 증가하는 부분수열 (LIS)의 길이를 출력
# 접근 : 현재위치를 마지막으로 하는 부분수열에서 
#       시작위치 ~ 현재위치직전까지의 수를 비교하며 
#       현재위치가 직전위치보다 큰 경우에만 dp테이블을 갱신한다

N = int(input())
lst = list(map(int, input().split()))
# print(lst)
d = [1] * N
for i in range(1,N) : 
     #print("i",i)
    for j in range(i) : 
        # print("j",j)
        if lst[i] > lst[j] : 
            d[i] = max(d[i],d[j]+1)
print(max(d))