def solution(phone_book):
    val = list(set(phone_book))
    phone_book = ','.join(val)
    count = 0
    for i in val:
        location = (phone_book.find(i))+1
        count += 1 if phone_book.find(i, location) != -1 else 0
    
    answer = False if count > 0 else True
    return answer