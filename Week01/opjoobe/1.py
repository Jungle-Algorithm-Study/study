# 신규 아이디 추천 # 풀이날짜 4월30일 # sol 소요시간 25 min

def solution(new_id):
    # step 1
    new_id_1 = new_id.lower()
    # step 2
    new_id_2 = ''.join([x for x in new_id_1 if x.isalnum() or x in ('-','_','.')])
    # step 3
    new_id_3 = ''
    i = 0 
    n = len(new_id_2)
    while i < n:
        new_id_3 += new_id_2[i]
        if new_id_2[i] == '.':
            while i< n and new_id_2[i] == '.':
                i += 1
        else:
            i += 1
    # step 4
    new_id_4 = new_id_3
    if new_id_4[0] == '.':
        new_id_4 = new_id_4[1:]
    if new_id_4 and new_id_4[-1] == '.':
        new_id_4 = new_id_4[:-1]
    # step 5
    new_id_5 = ''
    if not new_id_4:
        new_id_5 += 'a'
    else:
        new_id_5 = new_id_4
    # step 6
    new_id_6 = new_id_5[:15]
    new_id_6 = new_id_6[:-1] if new_id_6[-1]=='.' else new_id_6
    # step 7
    new_id_7 = new_id_6
    last_c = new_id_6[-1]
    while len(new_id_7) < 3:
        new_id_7 += last_c
    answer = new_id_7
    return answer