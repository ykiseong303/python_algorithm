'''
분류 : 다이나믹 프로그래밍
문제 : 가장 긴 바이토닉 부분 수열 (백준 11055)
작성일자 : 2021.07.05
'''

# 목적 : 가장 긴 바이토닉 부분 수열의 길이를 출력
# 접근 : dp
#       1. 가장 긴 감소하는 부분 수열의 dp테이블을 만든다
#       2. 가장 긴 증가하는 부분 수열의 dp테이블을 만든다
#       3. 두 dp테이블을 합치고 -1을 하면 바이토닉 수열을 만들 수 있다

N = int(input())
lst = list(map(int, input().split()))
d1 = [1]*N
d2 = [1]*N
res = 0
# 가장 긴 감소하는 부분 수열 만들기 
lst.reverse()
for i in range(N) : 
    for j in range(i) : 
        if lst[i] > lst[j] : 
            d2[i] = max(d2[i], d2[j]+1)
# 특정위치에서 증가하는 부분수열을 만들기
d2.reverse()
# print(d2)
lst.reverse()
for i in range(N) : 
    for j in range(i) : 
        if lst[i] > lst[j] : 
            d1[i] = max (d1[i], d1[j]+1)
    res = max(res,d1[i]+d2[i]) # 두 수열을 합치기
print(res-1) # 가운데 숫자는 중복되므로 -1을 해줘야 함
