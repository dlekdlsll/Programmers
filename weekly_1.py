def solution(price, money, count):
    fare = 0
    for i in range(1,count+1):
        price_multiple = price*i
        fare = fare + price_multiple
    if money - fare > 0:
        answer = 0
    else:
        answer = fare - money
    return answer