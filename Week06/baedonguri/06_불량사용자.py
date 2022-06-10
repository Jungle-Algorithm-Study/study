# [프로그래머스] 불량 사용자 Python
# https://programmers.co.kr/learn/courses/30/lessons/64064

from itertools import permutations
def check(user, banned):
    if len(user) != len(banned):
        return False

    for i in range(len(banned)):
        if banned[i] == '*':
            continue
        if banned[i] != user[i]:
            return False
    return True

def solution(user_id, banned_id):
    dap = []
    for perm in permutations(user_id, len(banned_id)):
        answer = []
        for user, ban in zip(perm, banned_id):
            if check(user, ban): 
                answer.append(user)
            else: 
                break

        if len(answer) == len(banned_id):
            answer.sort()
            if answer not in dap:
                dap.append(answer)
    return len(dap)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]

print(solution(user_id, banned_id))

