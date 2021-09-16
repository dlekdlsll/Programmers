def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        ezin = str(bin(i|j))[2:]
        while len(ezin) != n: ezin = '0'+ezin      # 이렇게 안하고 replace쓰면 다 해결되는데...
        result = ''
        for k in ezin: result += '#' if k == '1' else ' '
        answer.append(result)
    return answer