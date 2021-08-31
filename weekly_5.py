def solution(word):
    from itertools import product

    Dict = ["A", "E", "I", "O", "U"]
    Dict2 = []
    for i in range(1, 6):
        for j in product(Dict, repeat = i):
            result = ''.join(j)
            Dict2.append(result)
    Dict2.sort()

    answer = Dict2.index(word)+1
    return answer