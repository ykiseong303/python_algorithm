'''
분류 : 다이나믹 프로그래밍
문제 : 계단오르기 (백준 2579)
작성일자 : 2021.05.31
'''

# 목적 : 계단의 끝에 도착했을 때 최대점수 출력
# 접근 : 시작위치에서부터 초기 값까지 설정
#       초기 값 이후의 값에 대해 점화식 설정
#       마지막 계단은 무조건, 세번연속금지의 규칙에 맞게 

N = int(input()) 
# 입력받을 리스트를  N의 최대개수까지 생성
lst = [0] * 300 # 301까지이고 인덱스는 0부터이므로 300까지 생성
d = [0] * 300 # dp테이블 
for i in range(N) : 
    lst[i] = int(input())
# dp테이블의 초기값 설정
d[0] = lst[0]
d[1] = lst[0]+lst[1]
# 3번째 칸에 도달하는 경우는 시작위치 + 1번째 + 3번째 혹은 시작위치 + 2번째 + 3번째
# 0,1이 안되는 이유는 3번째 위치를 포함시켜야 하는데,
# 그러면 세칸 연속이 되므로 규칙에 어긋남
d[2] = max(lst[2]+lst[0],lst[2]+lst[1])
for i in range(3,N) : # N이 3이하인 경우 for문은 실행되지 않음
    # i번째에 도달하는 경우는 한칸 전 혹은 두칸 전에서 도달하는 2가지 경우
    # 2칸전에서 도착하는 경우는 상관x
    # 1칸전에서 도착하는 경우는 2칸전 > 1칸전 > 현재로 도달(3번연속위반)할 수 있으므로
    # 또한 마지막 계단은 무조건 밟아야 하기 때문에 
    # 완전한 최댓값이 아니더라도 
    # 현재위치 + 직전위치 + 직전위치를 두칸 건너온 위치까지의 최적해로 구함
    d[i] = max(lst[i]+d[i-2], lst[i]+lst[i-1]+d[i-3]) 
print(d[N-1])
