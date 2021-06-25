#[?] 1부터 1,000까지의 정수 중 13의 배수의 갯수(건수, 횟수)

# 갯수 알고리즘(Count Algorithm) : 주어진 범위에 주어진 조건에 해당하는 자료들의 갯수

#[1] Input
count = 0 # 갯수를 저장할 변수를 0으로 초기화

#[2] Process : 갯수 알고리즘의 영역 -> 주어진 범위에 주어진 조건(필터링)
for i in range(1,1000): #주어진 범위
    if i % 13 == 0: #주어진 조건: 13의 배수면 갯수를 증가
        # count = count + 1
        count += 1 #count 변수

#[3] Output
print(f'1부터 1,000까지의 정수 중 13의 배수의 개수 : {count}')