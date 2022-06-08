# 불량사용자 # 프로그래머스 # 35min sol 

# 부정응모한 응모자들은 모아서, 당첨에서 제외
# 이때 개인정보 보호 위해 일부문자를 *로 가림 # 아이디당 최소 하나이상
# 불량 사용자 목록에 매핑된 응모자 아이디 => 제재 아이디

""" 첫번째 풀이 : 결국 permutation으로 타협해 일단 해결 """
import re
from itertools import permutations

def solution(user_id, banned_id):
    answer_set = set()
    banned_len = len(banned_id)
    
    for case in permutations(user_id, banned_len):
        flag = True
        for idx in range(banned_len):
            u_id = case[idx]
            b_id = banned_id[idx]
            b_id = b_id.replace('*','[\w]')
            p = re.compile(b_id)
            if not p.fullmatch(u_id):
                flag = False
                break
        if flag:
            case = sorted(list(case))
            answer_set.add(tuple(case))

    answer = len(answer_set)
    return answer

""" 두번째 풀이: 조합의 갯수를 구하는 함수 nCr, 여러 리스트의 조합을 만드는 함수 product를 활용 """
import re
from itertools import permutations, product
import operator as op
from functools import reduce

def nCr(n, r): # 이건 구현하기 귀찮아서 걍 인터넷에서 가져옴...^^;
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

def solution(user_id, banned_id):
    answer_set = set()
    banned_len = len(banned_id)
    match = [list() for _ in range(banned_len)]
    # 각 banned)id 별로 매칭되는 아이디의 리스트를 만들어줌
    for idx in range(banned_len):
        b_id = banned_id[idx]
        b_id = b_id.replace('*','[\w]')
        p = re.compile(b_id)
        for u_id in user_id:
            if p.fullmatch(u_id):
                match[idx].append(u_id)
    
    # banned_id 별로 매칭된 아이디의 리스트가 모두 동일하다면
    if len(set(map(tuple,match)))==1:
        return nCr(len(match[0]), banned_len)

    # 그 외에는 product 함수로, 각 banned_id 별로 매칭된 아이디의 리스트들의 조합을 구해줌
    for i in product(*match):
        # 만약 조합 i 안에 중복이 존재하는 경우, i는 제재 리스트가 될 수 없음
        if banned_len != len(set(i)):
            continue
        case = sorted(list(i)) # 리스트로 바꿔 정렬하고 
        answer_set.add(tuple(case)) # 다시 튜플로 바꿔서 set 안에 넣어줌 (중복된 제재 리스트 제거)

    answer = len(answer_set)
    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]

print(solution(user_id, banned_id))