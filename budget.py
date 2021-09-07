def solution(d, budget):
    answer = 0
    while len(d) > 0:
        if min(d) <= budget:
            budget -= min(d)
            d.remove(min(d))
            answer += 1
        else:
            break
    return answer