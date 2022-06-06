def solution(enroll, referral, seller, amount):
    relation = {}
    money = {}
    
    # zip으로 관계 딕셔너리와 돈 계산 딕셔너리를 만들기
    for i,j in zip(enroll, referral):
        relation[i] = j
        money[i] = 0
        
    for s,a in zip(seller, amount):
        
        #칫솔은 하나에 100원
        a *= 100
        
        # 조직 타고 올라가면서 돈 계산하기
        while True:
            # 돈이 10원 아래면 넣고 끝남
            if a < 10:
                money[s] += int(a)
                break
            # 10원 이상이라면
            else:
                # 10퍼센트 떼주기
                t = int(0.1*a)
                # 12원 일경우 1원만 떼줘야 하므로 int로 1원만 떼어서 
                # 12-1 해줘야함
                money[s] += a-t
                
                # a는 10퍼센트인 t로 다시 초기화
                a = t
            # 다단계 타고 올라갔더니 "-" 면 break
            if relation[s] == '-':
                break
                
            # 다단계 타고 올라가서 다시 반복
            s = relation[s]
    
    # 돈 밸류값만 리턴
    return [*money.values()]