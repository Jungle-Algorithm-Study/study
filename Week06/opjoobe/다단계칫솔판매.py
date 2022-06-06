# 프로그래머스 # 다단계 칫솔 판매 # 50min sol

# 첫번째 풀이 깔끔히 줄인 버전
from collections import defaultdict
def solution(enroll, referral, seller, amount):
    answer = []

    data_length = len(seller)
    answer_D = defaultdict(int)
    enroll_D = {member:refer for member,refer in zip(enroll, referral)}

    for name, quantity in zip(seller, amount):
        now_D = defaultdict(int)
        total = quantity*100
        while True:
            ref = enroll_D[name] 
            give = total//10
            get = total-give
            now_D[name] = get
            if ref == '-': break
            now_D[ref] = give
            name, total = ref, give
            if not total: break

        for member,get in now_D.items():
            answer_D[member] += get

    answer = [answer_D[member] for member in enroll]
    return answer

# 첫번째 풀이 # 태초마을 #지저분...
from collections import defaultdict
def solution(enroll, referral, seller, amount):
    answer = []
    data_length = len(seller)
    ''' 판매데이터 완성 '''

    answer_D = defaultdict(int)
    enroll_D = defaultdict(str)
    enroll_length = len(enroll)
    for i in range(enroll_length):
        member = enroll[i]
        refer = referral[i]
        enroll_D[member] = refer
    # print(enroll_D)
    ''' 추천인 완성 '''

    for i in range(data_length):
        name = seller[i]
        quantity = amount[i]
        # print(f"name : {name}")
        total = quantity*100
        now_D = defaultdict(int)
        while True:
            ref = enroll_D[name]
            give = total//10
            rest = total-give
            # print(give, rest)
            now_D[name] = rest
            if ref == '-':
                break
            now_D[ref] = give
            name = ref
            total = give
            if not total: break
        # print(now_D)
        for k,v in now_D.items():
            answer_D[k] += v
        
    
    for e in enroll:
        answer.append(answer_D[e])
    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))
