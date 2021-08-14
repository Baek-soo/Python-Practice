def solution(board, moves):
    bucket = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                bucket.append(board[j][i-1])
                board[j][i-1] = 0
                if len(bucket) > 1:
                    if bucket[-1] == bucket[-2]:
                        bucket.pop(-1)
                        bucket.pop(-1)
                        answer +=2
                break
    return answer