def solution(lottos, win_nums):
    result = 0
    for i in lottos:
        try:
            if win_nums.index(i) != -1: result += 1
        except: result += 0
    blind = len([i for i in lottos if i == 0])
    lotto_result = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    print(max(result+blind, result))
    return [lotto_result[max(result+blind, result)], lotto_result[min(result+blind, result)]]