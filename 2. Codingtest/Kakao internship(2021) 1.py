def solution(s):
    answer = ''
    numbers = {'zero':'0', 'one':(1,0), 'two':(2,0), 'three':(3,0), 'four':(4,0), 'five':(5,0), 'six':(6,0), 'seven':(7,0), 'eight':(8,0), 'nine':(9,0)}

    for i in s:
        if i in numbers:
            answer += numbers[0]
        else:
            answer += i




    return answer


print(solution(123))
#이거 풀어야함