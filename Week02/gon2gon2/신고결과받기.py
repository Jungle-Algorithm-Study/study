# 첫번째
def solution(id_list, report, k):
    answer = []
    reported = {name:set() for name in id_list}
    max_k = 0
    ban = set()
    for r in report:
        _from, _to = r.split()
        reported[_to].add(_from)
        n = len(reported[_to])
        if n == k:
            ban.add(_to)
    if ban:
        answer = {name:0 for name in id_list}
        for b in ban:
            for reporter in reported[b]:
                answer[reporter] += 1
                
        return list(answer.values())
    return [0,0]



# 두번째
def solution(id_list, report, k):
    from collections import defaultdict
    
    mail_count = {name:0 for name in id_list}
    reported_reporter = defaultdict(set)
    ban = set()
    
    for r in report:
        reporter, reported = r.split()
        reported_reporter[reported].add(reporter)
        if len(reported_reporter[reported]) >= k:
            ban.add(reported)
    
    
    for b in ban:
        for reporter in reported_reporter[b]:
            mail_count[reporter] += 1
            
    answer = [mail_count[name] for name in id_list]
    
    return answer
