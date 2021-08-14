def solution(arr):
    answer = []; arr += ['#']
    for i in range(0, len(arr)-1):
        if arr[i] != arr[i+1]: answer.append(arr[i])
    return answer