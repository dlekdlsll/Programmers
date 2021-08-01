def solution(board, moves):
    answer = 0; result = []
    for i in moves:
        for j in range(0,len(board)):
            x = board[j][i-1]
            if x == 0 : continue
            result.append(x)
            board[j][i-1] = 0
            break
        
        if len(result)>1 and result[-1]==result[-2]:           
            del result[-2:]
            answer += 2
        
    return answer