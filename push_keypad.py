def solution(numbers, hand):
    
    def manhattan(p1, p2):
        d = 0
        for i in range(len(p1)):
            d += abs(p1[i] - p2[i])
        return d
    
    answer = ''
    finger = {1:[0, 0], 4:[1, 0], 7:[2, 0], '*':[3, 0], 2:[0, 1],5:[1, 1],8:[2, 1],0:[3, 1],3:[0, 2],6:[1, 2],9:[2, 2],'#':[3, 2]}
    L_finger = finger['*']; R_finger = finger['#']
    
    for i in numbers:
        if i in (1, 4, 7):
            L_finger = finger[i]
            answer += 'L'
        elif i in (3, 6, 9):
            R_finger = finger[i]
            answer += 'R'
        else:
            if manhattan(finger[i], L_finger) == manhattan(finger[i], R_finger):
                if hand == 'left':
                    L_finger = finger[i]
                    answer += 'L'
                else:
                    R_finger = finger[i]
                    answer += 'R'
            elif manhattan(finger[i], L_finger) > manhattan(finger[i], R_finger):
                R_finger = finger[i]
                answer += 'R'
            else:
                L_finger = finger[i]
                answer += 'L'
    return answer