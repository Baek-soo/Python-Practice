#[?] 주어진 데이터 중에서 가장 작은 [짝수] 값
import sys
#최솟값 알고리즘(Min Algorithm): (주어진 범위 + 주어진 조건)의 자료들의 가장 작은 값
def main():
    #[0] Initialize
    min = sys.maxsize # 숫자 형식의 데이터 중 가장 큰 값으로 초기화

    #[1] Input
    numbers = [ 2, 5, 3, 7, 1 ]; #min : 1 -> 짝수 min : 2
    N = len(numbers) #의사코드(슈도코드)

    #[2] Process : min algorithm
    for i in range(0,N):
        if numbers[i] < min and numbers[i] % 2 == 0:
            min = numbers[i] 

    #[3] Output 
    print(f'짝수 최솟값 : {min}')

    pass


if __name__  == "__main__":
    main()