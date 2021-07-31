import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-\_\.]', '', new_id)
    new_id = re.sub('[\.]+', '.',new_id)
    new_id = new_id.strip('.')
    if len(new_id)==0 : new_id = 'a'
    elif len(new_id)>15 : new_id = new_id[0:15]
    new_id = new_id.strip('.')
    while len(new_id) < 3 : new_id = new_id + new_id[-1]
    answer = new_id
    return answer