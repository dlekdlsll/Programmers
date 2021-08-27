def solution(n):
    result = list(str(n))
    result = sorted(result, reverse = True)
    
    answer = ''
    for i in result:
        answer += str(i)
    answer = int(answer)
    
    return answer