#[?] N명의 점수중에서 80점 이상 95점 이하인 점수의 평균

# 평균 알고리즘(Average Algorithm) : 주어진 범위에 주어진 조건에 해당하는 자료들의 평균

#[1] Input
data = [ 90, 65, 78, 50, 95 ]
sum = 0 # 합계 담는 그릇
count = 0 # 갯수 담는 그릇
N = len(data) # 의사코드(슈도코드)

#[2] Process : AVG = SUM / COUNT
for i in range(0, N):
    if data[i] >= 80 and data[i] <= 95: #주어진 조건
        sum += data[i] #sum 알고리즘 -> sum = sum + data[i]
        count += 1 #count

avg = 0.0
if sum != 0 and count != 0:
    avg = sum/count #Average

#[3] Output
print(f'80점 이상 95점 이하인 자료들의 평균 : {avg:.2f}')