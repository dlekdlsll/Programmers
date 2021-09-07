def solution(N, stages):
    result = [[i for i, x in enumerate(stages) if x == j] for j in range(1, N+1)]
    result_2 = []; steps = 0
    for i, j in enumerate(result):
        if len(stages) - steps != 0:
            result_2.append((i+1, len(j)/(len(stages) - steps))) 
            steps += len(j)
        else : result_2.append((i+1, 0))
    answer = [i[0] for i in sorted(result_2, key = lambda x: x[1], reverse = True)]
    return answer