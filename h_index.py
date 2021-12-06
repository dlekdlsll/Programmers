def solution(citations):
    count = len(citations)
    for h in sorted(citations, reverse = True):
        up = len([i for i in citations if i >= h])
        dn = len([i for i in citations if i < h])
        if up == h and up + dn == count:
            return h