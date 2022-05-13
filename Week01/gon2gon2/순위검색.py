def solution(info, query):
    answer = []
    from collections import defaultdict
    from itertools import combinations
    from bisect import bisect_left
    
    
    # 1. key: int[] 형태의 테이블을 만든다.
    # key는 필터조건(condition)이, value로는 해당 조건을 만족하는 지원자의 점수를 넣는다.
    table = defaultdict(list)
    
    for i in info:
        *info_condition, info_score = i.split()
        info_score = int(info_score)
        
        
        # 0개부터 n-1개까지 -로 replace된 경우를 체크해줘야함 -> combinations 사용
        for n in range(5):
            set_for_replace = set(combinations((0,1,2,3),n))
            
            for replace_set in set_for_replace:
                temp_condition = info_condition[:]
                
                # - 처리
                for r in replace_set:
                    temp_condition[r] = '-'
                
                info_key = ''.join(temp_condition)
                table[info_key].append(info_score)
         
        
    # 2.이분탐색을 위해 정렬
    for v in table.values():
        v.sort()
                
                
                
    # 3. q조건을 만족하는 점수 리스트에서 기준보다 낮은 점수의 인덱스를 구하고,
    # 조건을 만족하는 모든 사람들의 수에서 빼준다.
    for q in query:
        *query_condition, query_score = q.replace('and ','').split()
        query_score = int(query_score)
        
        query_key = ''.join(query_condition)
        query_result = table[query_key]
        
        
        lower_bound = bisect_left(query_result, query_score)
        
        answer.append(len(query_result) - lower_bound)
    

    return answer
