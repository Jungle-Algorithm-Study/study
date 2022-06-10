def solution(enroll, referral, seller, amount):
    answer = []
    parent_dict = {}
    for i in range(len(enroll)) :
        parent_dict[enroll[i]] = referral[i]
    profit_dict = {key: 0 for key in enroll}
    
    for i, sell in enumerate(amount):
        current = seller[i]
        parent = parent_dict[current]

        total_profit = sell * 100
        mother_profit = total_profit // 10
        own_profit = total_profit - mother_profit

        profit_dict[current] += own_profit

        while parent != "-" and mother_profit >= 1:
            total_profit = mother_profit
            mother_profit = total_profit // 10
            own_profit = total_profit - mother_profit
            
            current, parent = parent_dict[current], parent_dict[parent]
            
            profit_dict[current] += own_profit
    
    answer = list(profit_dict.values())

    return answer
