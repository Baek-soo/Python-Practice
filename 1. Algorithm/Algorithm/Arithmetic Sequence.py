#[?] 1부터 20까지의 정수 중 홀수의 합을 구하는 프로그램

# 등차수열(Arithmetic Sequence) : 연속하는 두 수의 차이가 일정한 수열

#[1] Input
sum = 0 #합계 알고리즘은 보통은 SUM을 0으로 만들고 시작


#[2] Process
for i in range(1, 20) : # 주어진 범위
    if i % 2 != 0: # 주어진 조건 : 필터링(홀수)
        sum = sum + i
        print(i, end = ', ') 
        
#[3] Output
print(f'\n1부터 20까지 홀수의 합은 : {sum}')