def solution(array, commands):
    return [sorted(array[c[0] -1 : c[1]])[c[2] - 1]for c in commands]



array = [1,5,2,6,3,7,4]
commands = [[2,5,3], [4,4,1], [1,7,3]]
answer = solution(array, commands)
print(answer)
