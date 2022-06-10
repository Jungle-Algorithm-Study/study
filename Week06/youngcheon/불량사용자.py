import re
from itertools import permutations
def solution(user_id, banned_id):
    b = '/'.join(banned_id).replace('*','.{1}')
    answer = set()
    for i in permutations(user_id, len(banned_id)):
        if re.fullmatch(b, '/'.join(i)):
            answer.add(''.join(sorted(i)))
    return len(answer)