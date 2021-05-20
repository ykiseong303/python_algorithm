'''
분류 : 다이나믹 프로그래밍
문제 : 개미전사 (이코테 예제1)
작성일자 : 2021.05.20
'''

# 목적 : 개미가 얻을 수 있는 식량의 최댓값을 출력
# 접근 : i-1번째와 i-2번째 + i번째 식량 중 최댓 값을 출력한다 (DP)

# 탑다운 방식
def ant(x) : 
     #print(x)
    if x == 1 :
        return d[0]
    if x == 2 : 
        return d[1] 
    if d[x] != 0 : # 이미 계산한 경우라면
        return d[x] # 계산된 값을 리턴
    # 탑다운 방식(아래로 내려가며 기록된 값이 있으면 그걸 사용)
    d[x] = max(ant(x-1), ant(x-2)+lst[x-1])
    return d[x] # x번째의 최적해를 리턴
N = int(input())
lst =  list(map(int, input().split()))
d = [0] * 100
d[0] = lst[0]
d[1] = max(lst[0],lst[1])
print(ant(N))

# 바텀업 방식
'''N = int(input())
lst = list(map(int, input().split()))
# 입력받는 리스트는 0번부터이므로 
d = [0] * 100 # 계산 결과를 기록하기 위한 DP테이블
d[0] = lst[0]
d[1] = max(lst[0],lst[1]) # 2번째 까지 중 최댓 값 (1,2중 1개)

for i in range(2,N) : 
    # 작은 문제들로 시작하여 차례대로 큰 문제를 해결
    d[i] = max(d[i-1],d[i-2]+lst[i]) # 직전에 턴 경우와, 그렇지 않은 경우(현재위치 플러스) 중 큰 값을 저장
    # res = max(d[i-1],d[i-2]+lst[i])
print(d[N-1])'''