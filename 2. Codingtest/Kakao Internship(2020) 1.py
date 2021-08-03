#key_pad left/right hand

def solution(numbers, hand):
    answer = ''
    
    key_pad = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,1), 8:(2,2), 9:(2,3), '*':(3,0), 0:(3,1), '#':(3,2)}

    left = [1, 4, 7]
    right = [3, 6, 9]
    lhand = '*'
    rhand = '#'

    for i in numbers: #1, 4, 7
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right: #3, 6, 9
            answer += 'R'
            rhand = i
        else: #2, 5, 8, 0
            curpos = key_pad[i]
            lpos = key_pad[lhand]
            rpos = key_pad[rhand]
            #오른손과 숫자의 거리
            l_dist = abs(curpos[0] - lpos[0]) + abs(curpos[1] - lpos[1])
            #왼손과 숫자의 거리
            r_dist = abs(curpos[0] - rpos[0]) + abs(curpos[1] - rpos[1])
            #왼손이 오른손보다 짧을 때
            if l_dist < r_dist:
                answer += 'L'
                lhand = i
            #오른손이 왼손보다 짧을 때
            if r_dist < l_dist:
                answer += 'R'
                rhand = i
            #둘 사이의 거리 같을 경우 
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i


    return answer


