def solution(array, commands):
    answer = []
    for com in commands:
        i, j, k = map(int, com)
        result = array[i-1:j]
        result.sort()
        answer.append(result[k-1])
    return answer