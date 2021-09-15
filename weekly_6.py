def solution(weights, head2head):
    win = []; out = []
    for i in head2head:
        try: win.append(i.count('W')/(len(i)-i.count('N')))
        except: win.append(0)

    for i in range(0, len(head2head)):
        x = 0
        for j in range(0, len(head2head)):
            if weights[i] < weights[j] and head2head[i][j] == 'W': 
                x += 1
        out.append(x)

    result = [(i+1,j[0],j[1], j[2]) for i, j in enumerate(zip(weights, win, out))]
    print(sorted(result, key = lambda x: (x[2], x[3], x[1]), reverse = True))

    return [i[0] for i in sorted(result, key = lambda x: (x[2], x[3], x[1]), reverse = True)]