def solution(land):
    answer = max(land[0])
    loc = land[0].index(max(land[0]))
    for i in land[1:]:
        res = max([j for j in i if i.index(j)!=loc])
        loc = i.index(res)
        answer =+ res
    return answer