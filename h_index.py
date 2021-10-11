def solution(citations):
    citations.sort(reverse = True)
    for i, j in enumerate(citations, start = 1):
        if i >= j:
            return citations[i-1]