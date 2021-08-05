def solution(array, commands):
    return [sorted(array[c[0] -1 : c[1]])[c[2] - 1]for c in commands]

#미친 문제 풀이
# def solution(array, commands):    
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
