# from collections import defaultdict
import math
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
sellers = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

# def solution(enroll, referral, sellers, amount):
    # enroll_dict = defaultdict(list)
    # refer_dict = defaultdict(list)

    # for p in enroll:
    #     enroll_dict[p] = 0

    # for i in range(len(enroll)):
    #     if referral[i] != "-":
    #         refer_dict[referral[i]].append(enroll[i])


    # for i in range(len(sellers)):
    #     earn = amount[i] * 100
    #     for refer in refer_dict.items():
    #         for j in refer[1]:
    #             if sellers[i] == j:
    #                 enroll_dict[j] += math.ceil(earn * 0.9)
    #                 break
    #         enroll_dict[refer[0]] += math.floor(earn * 0.1)
    #     for parent in refer_dict.items():
    #         for child in parent[1]:
    #             enroll_dict[parent[0]] += int(enroll_dict[child] * 0.1)

    # defaultdict(<class 'list'>, {'john': 0, 'mary': 734, 'edward': 870, 'sam': 0, 'emily': 450, 'jaimie': 384, 'tod': 180, 'young': 1080})            

def solution(enroll, referral, sellers, amount):
    import math
    parentTree = dict(zip(enroll, referral))
    answer = dict(zip(enroll, [0 for i in range(len(enroll))]))

    for i in range(len(sellers)):
        earn = amount[i] * 100
        target = sellers[i]

        while True:
            if earn < 10:  # 10원 단위 이하라면 모두 받고 종료
                answer[target] += earn
                break
            else:          # 10%를 제외하고 받아줌
                answer[target] += math.ceil(earn * 0.9) # 상위가 없다면 종료
                if parentTree[target] == "-":
                    break
                earn = math.floor(earn * 0.1) # 10%는 중개인에게.
                target = parentTree[target]

    return list(answer.values())

print(solution(enroll, referral, sellers, amount))