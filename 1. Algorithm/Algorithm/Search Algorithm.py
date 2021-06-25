#[?] 정렬되어 있는 데이터를 이진 검색(이분 탐색)을 사용하여 반씩 나눠서 검색

#검색 알고리즘(Search Algorithm): 주어진 데이터에서 특정 데이터를 찾는 방법
def main():
    #[1] Input
    data = [1, 3, 5, 7, 9] #오름차순으로 정렬되었다고 가정, 랜덤으로 배열되어있다면 Sort Algorithm을 사용해여 정렬을 먼저 해주어야함
    N = len(data) #의사코드
    Search = 7 #검색할 데이터
    flag = False #플래그 변수 : 데이터를 찾으면 True, 못찾으면 False
    index = 0 #인덱스 변수 : 찾은 위치
    count = 1
    #[2] Process : 이진 검색(Binary Search) 알고리즘 Full Scan -> Index scan
    low = 0 #min: 낮은 인덱스
    high = N-1 #max: 높은 인덱스
    while low <= high:
        mid = int((low + high) / 2) # 중간 인덱스(mid) 구하기
        if data[mid] == Search: #중간 인덱스에서 찾기
            flag = True; index = mid; break; #찾으면 플래그, 인덱스 저장 후 종료
        if data[mid] > Search:
            high = mid - 1 #찾을 데이터가 작으면 왼쪽 영역으로 이동
            count += 1
        else:
            low = mid + 1 #찾을 데이터가 크면 오른쪽 영역으로 이동
            count += 1
    #[3] Output
    if flag:
        print(f"{Search}을(를) {index}위치에서 {count}번만에 찾았습니다.")
    else:
        print("찾지 못했습니다.")

    pass

if __name__ == "__main__":
    main()