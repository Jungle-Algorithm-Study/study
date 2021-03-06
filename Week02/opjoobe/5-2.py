# 2시30분시작 #sol 16min #신고결과받기
def solution(id_list, report, k):
    report_D = dict()
    ans_D = dict([(id,0) for id in id_list]) # {id:0 for id in id_list} 로도 가능
    for r in report:
        sender, receiver = r.split()
        if receiver in report_D.keys():
            report_D[receiver].append(sender)
        else:
            report_D[receiver] = [sender]
    answer = []
    for id in id_list:
        if id in report_D.keys():
            senders = set(report_D[id])
            if len(senders) >= k:
                for id in senders:
                    ans_D[id] += 1
    answer = list(ans_D.values())
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))