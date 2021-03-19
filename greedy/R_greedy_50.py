'''
분류 : 그리디 알고리즘
문제 : 회문 (백준 17609번)
작성일자 : 2021.03.19
'''
# 목적 : 입력된 문자가 회문인지 유사회문인지 아무것도 아닌지 출력한다
# 접근 : 단어의 제일 왼쪽과 오른쪽에서 가운데방향으로 전진하며 비교한다 (투포인터)
#       왼쪽과 오른쪽에 있는 것부터 비교를 하는 방식인데 
#       가장 끝에서부터 비교해서 그리디인지? 

T = int(input())

def secondCheck(word,left,right) : 
    while left < right : 
        if word[left] == word[right] : 
            left += 1 
            right -= 1 
        else : 
            # 한글자 건너 뛰었음에도 같지 않다면 유사회문이 아님
            return 2 
    # 한글자 건너뛰고 같으므로 유사회문임
    return 1

def firstCheck(word,left,right) : 
    while left < right : # 단어의 중간까지만 가기 위해서 
        if word[left] == word[right] : 
            left += 1 
            right -= 1 
        else : # 유사회문인지 검사 
            # 유사회문은 단어 한글자만 지워여 하므로, 
            # 왼쪽과 오른쪽 각각 한글자씩 건너뛰어서 검사
            # 건너뜀으로써 지운 것처럼 생각하기
            temp1 = secondCheck(word,left+1,right)
            temp2 = secondCheck(word,left,right-1)
            return min(temp1,temp2)
    return 0

for _ in range(T) : 
    data = input()
    left = 0
    right = len(data) -1 
    ans = firstCheck(data,left,right)
    print(ans)