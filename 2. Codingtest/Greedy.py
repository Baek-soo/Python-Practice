def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in lost:
        if i in reserve:
            answer += 1
            reserve.remove(i)
            continue
        for j in reserve:
            if j == i-1:
                answer += 1
                reserve.remove(j)
                break
            elif j == i+1:
                if j in lost:
                    break
                answer += 1
                reserve.remove(j)
                break
    return answer