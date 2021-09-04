def solution(numbers, hand):
    import numpy as np
    answer = ''
    keypad = np.array([[ (x, y) for x in (0, 1, 2) ] for y in (0, 1, 2, 3)])
    finger = {1:[0, 0], 4:[1, 0], 7:[2, 0], '*':[3, 0], 2:[0, 1],5:[1, 1],8:[2, 1],0:[3, 1],3:[0, 2],6:[1, 2],9:[2, 2],'#':[3, 2]}
    L_finger = finger['*']; R_finger = finger['#']
    
    for i in numbers:
        if i in (1, 4, 7):
            L_finger = finger[i]
            answer += 'L'
        elif i in (3, 6, 9):
            R_finger = finger[i]
            answer += 'R'
        elif i in (2, 5, 8, 0):
            if abs(sum(np.array(L_finger))) == abs(sum(np.array(R_finger))):
                if hand == 'right':
                    answer += 'R'
                    R_finger = finger[i]
                else:
                    answer += 'L'
                    L_finger = finger[i]
            elif abs(sum(np.array(L_finger))) > abs(sum(np.array(L_finger))):
                answer += 'R'
                R_finger = finger[i]
            elif abs(sum(np.array(L_finger))) < abs(sum(np.array(L_finger))):
                answer += 'L'
                L_finger = finger[i]
    return answer