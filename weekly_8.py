def solution(sizes):
    w, h = 0, 0

    for i in sizes:
        if w < max(i[0],i[1]): w = max(i[0],i[1])
        if h < min(i[0], i[1]): h = min(i[0], i[1])

    return w*h