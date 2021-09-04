def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        for j in numbers[-1:i:-1]:
            answer.append(numbers[i] + j)
    answer = sorted(list(set(answer)))
    return answer