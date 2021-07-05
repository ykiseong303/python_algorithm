'''
분류 : 다이나믹 프로그래밍
문제 : 포도주 시식 (백준 2156)
작성일자 : 2021.07.05
'''

# 목적 : 마실 수 있는 포도주의 최대 양을 출력
# 접근 : dp
#       1. 이전 문제가 다음 문제를 해결
#       2. 부분 중복 문제
#       연속으로 3칸이 되지 않는 한에서, 현재위치에서 고를 수 있는건 두칸전의 최대 or 바로직전값+3칸이후 중 최대 값
#       계단 수(2579) 문제는 현재 위치에서 다음, 다다음만 움직일 수 있는 제약이 있지만
#       이 문제는 그런 제약은 존재하지 않으므로, 연속되지 않는 한에서 최대의 값을 찾아야 함
#####       현재 위치를 마시지 않는 경우도 고려 해야함. (항상 마지막에서 끝나야 하는 것이 아니므로)
N = int(input())
lst = []
for _ in range(N) : 
    lst.append(int(input()))
if N == 1 : 
    print(*lst)
elif N == 2 : 
    print(sum(lst))
elif N == 3 : 
    print(max(lst[0]+lst[1], lst[1]+lst[2],lst[0]+lst[2]))
else : 
    d = [0] * N 
    d[0] = lst[0]
    d[1] = lst[0]+lst[1]
    d[2] = max(lst[0]+lst[1], lst[1]+lst[2],lst[0]+lst[2])
    for i in range(3, N) : 
        # temp = d[:i-2]
        d[i] = max(lst[i]+d[i-2], lst[i]+lst[i-1]+d[i-3],d[i-1])
        #d[i] = lst[i] + max(lst[i-1]+max(temp),d[i-2])
    # print(d)
    print(max(d))