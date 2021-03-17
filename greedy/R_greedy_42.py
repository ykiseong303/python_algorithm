'''
분류 : 그리디 알고리즘
문제 : 주사위 (백준 1041번)
작성일자 : 2021.03.17
'''

# 목적 : 주사위 N의 3제곱 개가 있을 때, 이를 잘 쌓아서 보이는 5면 합의 최솟값
# 접근 : 주사위의 값중 마주하는 값들끼리 중 가장 작은 값이 보이게 한다
#       A-F, E-B, C-D의 면은 서로 마주하고 있다
#       주사위는 마주하는 면을 제외하고 모든 면과 이어져 있다

N = int(input())
dice = list(map(int, input().split()))

if N == 1 : 
    # 주사위가 1개라면 가장 큰 값을 뺴면 된다
    dice.pop(dice.index(max(dice)))
    print(sum(dice))
else : 
    m = []
    # 마주하는 값중의 최소 값을 지정한다
    min1 = m.append(min(dice[0],dice[5]))
    min2 = m.append(min(dice[1],dice[4]))
    min3 = m.append(min(dice[2],dice[3]))
    m.sort()
    # 마주하는 면만 아니면 1면 ~ 3면의 조합이 모두 가능하므로
    # 각각의 경우의 최소가 되는 경우를 구해준다
    m1 = min(m) # 1면만 보이는 경우
    m2 = m[0] + m[1] # 2면이 보이는 경우
    m3 = sum(m) # 3면이 보이는 경우
    
    case1 = (N-2)*4*(N-1)*m1 + pow(N-2,2)*m1
    case2 = 4*m2*(N-1) + m2*4*(N-2)
    case3 = 4*m3

    print(case1+case2+case3)













'''
dice_2 = [] 
# 주사위 두개를 뽑아서 만들 수 있는 경우의 수 
for i in range(0,6,5) : 
    for j in range(1,6) : 
        if (i == 0 and j == 5) or (i == 5 and j == 0) or (i==5 and j==5) :
            continue
        # print(dice[i],dice[j])
        dice_2.append(dice[i]+dice[j])
# print(dice_2)
dice_3 = []
for a in range(0,6,5) : 
    for b in range(1,5,3) :
        for c in range(2,4) : 
            dice_3.append(dice[a]+dice[b]+dice[c])
            # print(dice[a], dice[b], dice[c])
# print(dice_3)
dice_2_2 = []
for i in range(1,5,3) : 
    for j in range(0,6) : 
        if (i==1 and j==1)or(i==4 and j==4) or (i == 1 and j == 4) or (i == 4 and j == 1) or (i==5 and j==5) :
            continue
        # print(dice[i],dice[j])
        dice_2_2.append(dice[i]+dice[j])
dice_3_2 = []
for a in range(1,6,3) : 
    for b in range(0,6,5) :
        for c in range(2,4) : 
            dice_3_2.append(dice[a]+dice[b]+dice[c])
            # print(dice[a], dice[b], dice[c])
        


second_floor = min(dice_2.pop(dice_2.index(min(dice_2))), dice_2_2.pop(dice_2_2.index(min(dice_2_2))) )
third_floor = min(dice_3.pop(dice_3.index(min(dice_3))), dice_3_2.pop(dice_3_2.index(min(dice_3_2))))
    

if N == 1 : 
    dice.pop(dice.index(min(dice)))
    # print(dice)
    print(sum(dice))
elif N == 2 : 
    print(second_floor*4 + third_floor*4)
elif N >= 3 : 
    mini = dice.pop(dice.index(min(dice)))
    one = mini * (N-2) * (N-1) * 4
    two = second_floor * (N-2) * 4
    three = mini * pow(N-2,2)
    four = second_floor * 4 * (N-2)
    print(second_floor*4 + third_floor*4 + one + two + three + four)
'''