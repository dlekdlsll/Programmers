def solution(n):
    listinin = [int(x) for x in range(2,n+1)]

    prime = [False,False] + [True]*(n-1)
    for i in range(2,len(prime)):
        if prime[i] == True:
            for j in range(i*2,len(prime),i):
                prime[j] = False

    printprime = [i for i in listinin if prime[i]==True]

    answer = len(printprime)
    return answer