def solution(numbers, hand):
    answer = ''
    key_pad = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), '*':(3,0), 0:(3,1), '#':(3,2)}
    left = [1,4,7]
    right = [3,6,9]

    lhand = '*'
    rhand = '#'

    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            toMove = key_pad[i]
            l_pos = key_pad[lhand]
            r_pos = key_pad[rhand]
            l_dist = abs(toMove[0]-l_pos[0]) + abs(toMove[1]-l_pos[1])
            r_dist = abs(toMove[0]-r_pos[0]) + abs(toMove[1]-r_pos[1])

            if l_dist < r_dist:
                answer += 'L'
                lhand = i
            elif l_dist > r_dist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i


    return answer