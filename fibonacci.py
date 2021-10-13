def solution(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(sum(F[i-2:i]))
    return F[n] % 1234567