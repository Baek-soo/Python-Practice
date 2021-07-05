#n명의 점수 중에서 80점 이상인 점수의 합계

#[1] Input 영역
scores = [100, 75, 50, 37, 90, 95]
sum = 0 #합계가 저장될 그릇
N = len(scores) # 의사코드(슈도코드)

#[2] Process: 합게 알고리즘 영역: 주어진 범위에 주어진 조건(필터링)
for i in range(0, N): # 주어진 범위
    if scores[i] >= 80: # 주어진 조건
        sum = sum + scores[i] #sum 알고리즘 



#[3] Output 
print(f"{N}명의 점수 중 80점 이상의 총점: {sum}")

#[!] 디버거 사용해보기 : F9(중단점 설정) -> F5(실행) -> F11(한 단계씩 코드 실행) -> F5
